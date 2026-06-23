# 🗺️ Skills Map & Job Matching

This spec defines the **data model** and **scoring** that turn KSA competencies into a
**skills map** — the graph of what a learner must earn to qualify for a specific job — and a
**job-match score**.

Depends on the proficiency scale and tag format in [`ksa-taxonomy.md`](ksa-taxonomy.md).

---

## 1. Core entities

```
KSA Component ──< has many ── belongs to ──> Target KSA Profile (a ROLE/JOB)
      ▲                                                │
      │ evidenced by                                   │ matched against
      │                                                ▼
Learner KSA Profile (a PERSON) ──────── diff ─────> SKILLS MAP (the gaps)
                                                       │
                                                       │ closed by
                                                       ▼
                                              Micro-credentials / Atoms
```

### 1.1 KSA Component

The atomic, matchable unit. Same IDs flow through atoms, profiles, and the map.

```yaml
id: S-build-rest-endpoint        # stable, unique, type-prefixed (K-/S-/A-)
type: skill                      # knowledge | skill | ability
label: "Build & test a REST endpoint"
description: "Create, route, and test a CRUD REST endpoint with error handling."
framework_ref: "O*NET:15-1254.00 / SFIA:PROG"
prerequisites: [K-http-semantics, S-read-write-python]
related: [S-write-unit-tests]
```

### 1.2 Target KSA Profile (a role)

What a **job opportunity** requires. Each line = a component + the **minimum level** and a
**weight** (importance). `must_have` marks disqualifying gaps.

```yaml
role: "Junior Backend Developer"
source: "https://example.com/job/12345"          # posting, or framework role
framework_ref: "O*NET 15-1254.00 Web Developers"
validated_by: "mentor:@sancarbar / employer:AcmeCorp"   # human gate
requirements:
  - { ref: K-http-semantics,     min_level: 2, weight: 3, must_have: true }
  - { ref: S-build-rest-endpoint, min_level: 2, weight: 5, must_have: true }
  - { ref: S-write-unit-tests,    min_level: 2, weight: 4, must_have: true }
  - { ref: S-use-git,             min_level: 2, weight: 3, must_have: true }
  - { ref: A-adaptability,        min_level: 2, weight: 3, must_have: false }
  - { ref: A-collaboration,       min_level: 2, weight: 4, must_have: true }
```

### 1.3 Learner KSA Profile (a person)

What the learner **has evidenced**. Each achieved level must point to evidence
(badge, artifact, assessment) — *no evidence, no level*.

```yaml
learner: "ada-learner-001"
evidenced:
  - { ref: K-http-semantics,     level: 2, evidence: "badge:mc-rest-api", verified: true }
  - { ref: S-build-rest-endpoint, level: 1, evidence: "lab:rest-lab-1",    verified: true }
  - { ref: S-use-git,             level: 2, evidence: "badge:mc-git-basics", verified: true }
  - { ref: A-collaboration,       level: 2, evidence: "360:cohort-7",       verified: true }
  # S-write-unit-tests: absent (level 0)
  # A-adaptability: absent (level 0)
```

---

## 2. The Skills Map (gap graph)

The skills map is the **diff** between a target profile and a learner profile, expressed as
a prerequisite-ordered graph of **gaps**.

For each requirement `r`:

```
gap(r) = max(0, r.min_level − learner.level(r.ref))
status =
   met        if gap == 0
   partial    if 0 < gap and learner.level > 0
   missing    if learner.level == 0
   blocker    if status != met and r.must_have == true
```

### Example skills map (from the profiles above)

| Component | Type | Need | Have | Gap | Status | Must-have |
| --------- | ---- | ---- | ---- | --- | ------ | --------- |
| K-http-semantics | 🧠 K | L2 | L2 | 0 | ✅ met | yes |
| S-build-rest-endpoint | 🛠️ S | L2 | L1 | 1 | 🟡 partial | yes |
| S-write-unit-tests | 🛠️ S | L2 | L0 | 2 | 🔴 missing | yes |
| S-use-git | 🛠️ S | L2 | L2 | 0 | ✅ met | yes |
| A-adaptability | 🌱 A | L2 | L0 | 2 | 🟡 missing | no |
| A-collaboration | 🌱 A | L2 | L2 | 0 | ✅ met | yes |

**To earn (ordered by prerequisite then weight):**
1. `S-build-rest-endpoint` L1→L2 *(close partial; prereq for the role's core task)*
2. `S-write-unit-tests` L0→L2 *(blocker — must_have)*
3. `A-adaptability` L0→L2 *(nice-to-have; raises match but not blocking)*

### Visual

```
        [K-http-semantics ✅]
                 │ prereq
                 ▼
   [S-build-rest-endpoint 🟡 L1→L2] ──► [S-write-unit-tests 🔴 L0→L2]  ◄ BLOCKER
                 │
                 ▼
        (capstone-ready)        [A-adaptability 🟡 L0→L2]  (boosts match)
        [S-use-git ✅] [A-collaboration ✅]
```

---

## 3. Job-match score

A single, explainable readiness number.

```
weighted_have(r)     = min(learner.level(r.ref), r.min_level) * r.weight
weighted_required(r) = r.min_level * r.weight

match_score = 100 * Σ weighted_have(r) / Σ weighted_required(r)

job_ready   = (match_score ≥ readiness_threshold)   AND
              (no must_have requirement has status != met)
```

- `readiness_threshold` default = **85%** (configurable per program/employer).
- A learner can be at 90% overall but **not job-ready** if a single `must_have` is unmet —
  surface blockers explicitly.

### Worked calculation (example above)

| Component | min×weight (req) | min(have,min)×weight (have) |
| --------- | ---------------- | --------------------------- |
| K-http-semantics | 2×3 = 6 | 2×3 = 6 |
| S-build-rest-endpoint | 2×5 = 10 | 1×5 = 5 |
| S-write-unit-tests | 2×4 = 8 | 0×4 = 0 |
| S-use-git | 2×3 = 6 | 2×3 = 6 |
| A-adaptability | 2×3 = 6 | 0×3 = 0 |
| A-collaboration | 2×4 = 8 | 2×4 = 8 |
| **Σ** | **44** | **25** |

`match_score = 100 × 25/44 ≈ 57%` → **not job-ready** (below 85% **and** two must-haves
unmet: `S-write-unit-tests`, plus `S-build-rest-endpoint` partial).

After earning the two blocking skills to L2: have = 25 + 5 + 8 = 38 → 38/44 ≈ **86%**, and
all must-haves met → **job-ready**. `A-adaptability` then becomes the next optional boost
(→ 44/44 = 100%).

---

## 4. KSA-balance health check

Because job postings over-index on Skills and under-state Abilities, the map should report
**coverage by type** so designers don't ship Knowledge-only paths:

```
coverage = { knowledge: met/total per type, skill: …, ability: … }
```

Warn if a role's map has **0 Abilities** (postings often omit them — add the durable
competencies the role really needs, validated by the employer/mentor).

---

## 5. Lifecycle of a learner's map

```
1. Pick target role            → load/extract Target KSA Profile (human-validated)
2. Self-assess + import badges  → Learner KSA Profile
3. Generate Skills Map + score  → gaps, blockers, ordered plan
4. Enroll in micro-credentials  → each maps to specific gap components
5. Produce evidence → assess    → verified levels updated
6. Re-score                     → repeat until job_ready
7. Export                       → portfolio + badges + match report to employer
```

---

## 6. Minimal JSON for tooling

A single object a Gen AI or app can produce/consume:

```json
{
  "role": "Junior Backend Developer",
  "readiness_threshold": 85,
  "match_score": 57,
  "job_ready": false,
  "blockers": ["S-write-unit-tests", "S-build-rest-endpoint"],
  "to_earn": [
    {"ref": "S-build-rest-endpoint", "from": 1, "to": 2, "type": "skill", "must_have": true},
    {"ref": "S-write-unit-tests", "from": 0, "to": 2, "type": "skill", "must_have": true},
    {"ref": "A-adaptability", "from": 0, "to": 2, "type": "ability", "must_have": false}
  ],
  "coverage": {"knowledge": "1/1", "skill": "1/3", "ability": "1/2"}
}
```

See [`../examples/skills-map-job-match-frontend.md`](../examples/skills-map-job-match-frontend.md)
for a complete end-to-end walkthrough on a real-style role.
