# 🧱 Micro-Credential v2 Schema (KSA-aware)

The machine-readable + human-readable format for an **ADA v2 micro-credential**. It is the
v1 [`micro-credential-ada-template.md`](../templates/micro-credential-ada-template.md) plus
a **YAML front matter** carrying KSA components, target levels, and skills-map links — so
the same file is readable by people *and* consumable by the skills-map / job-match tooling.

> **Rule:** the YAML front matter is the source of truth for matching; the Markdown body is
> the human-facing design. Keep KSA ids identical in both.

---

## 1. File anatomy

```
┌─ YAML front matter ─────────────┐   ← machine-readable (KSA, levels, links)
│  ---                            │
│  meta, role link, ksa[], atoms[]│
│  ---                            │
├─ Markdown body ─────────────────┤   ← human-readable (v1 template sections)
│  objectives, phase planner,     │
│  capstone, rubrics, resources   │
└─────────────────────────────────┘
```

---

## 2. YAML front matter schema

```yaml
---
schema: ada-microcredential/v2
id: mc-rest-api-fundamentals            # unique slug
title: "REST API Fundamentals with Flask"
language: en                            # en | es | pt-br
duration_hours: 18
status: draft                           # draft | reviewed | published
license: CC-BY-SA-4.0
authors: ["Ada School Team"]
mentors: ["@sancarbar"]

# --- job linkage (optional but enables matching) ---
target_roles:
  - role: "Junior Backend Developer"
    framework_ref: "O*NET 15-1254.00"
    source: "https://example.com/job/12345"

# --- KSA components this micro-credential develops ---
ksa:
  - id: K-http-semantics
    type: knowledge
    label: "HTTP request/response semantics & status codes"
    target_level: 2                     # 0–4 (see ksa-taxonomy.md §4)
    bloom: understand
    framework_ref: "SFIA:PROG"
  - id: S-build-rest-endpoint
    type: skill
    label: "Build & test a CRUD REST endpoint"
    target_level: 2
    bloom: create
    primary: true
    prerequisites: [K-http-semantics]
  - id: S-write-unit-tests
    type: skill
    label: "Write unit tests for an endpoint"
    target_level: 2
    bloom: apply
  - id: A-adaptability
    type: ability
    label: "Adapt the API when requirements change"
    target_level: 2
    affective_stage: respond            # receive|respond|value|organize|internalize
    assessed_occasions: 3               # abilities need ≥3
  - id: A-collaboration
    type: ability
    label: "Collaborate via code review"
    target_level: 2
    affective_stage: value
    assessed_occasions: 3

# --- atoms, each tagged to KSA + phase ---
# `modalities` pick concrete sub-types from specs/learning-atom-topology.md
# Each entry: {dimension: read|listen|watch|see|practice|evaluate|collaborate, subtype: "..."}
atoms:
  - id: atom-1
    title: "How the web talks: HTTP & REST"
    objective: "Explain HTTP methods, status codes, and REST resource design."
    ksa_refs: [K-http-semantics]
    phase: 1                            # 1–4
    modalities:
      - { dimension: read,     subtype: "Technical Article" }
      - { dimension: watch,    subtype: "Video Explainer" }
      - { dimension: see,      subtype: "Diagram" }
      - { dimension: evaluate, subtype: "Pop Quiz" }
    deliverable: "Concept check (quiz) + annotated request/response diagram"
    rubric: knowledge-mini
  - id: atom-2
    title: "Build your first endpoint"
    objective: "Create and test a CRUD endpoint in Flask."
    ksa_refs: [S-build-rest-endpoint, K-http-semantics]
    phase: 3
    modalities:
      - { dimension: watch,    subtype: "Tutorial / Screencast" }
      - { dimension: practice, subtype: "Codelab" }
      - { dimension: evaluate, subtype: "Performance Task" }
    deliverable: "Working /items CRUD endpoint in a repo"
    rubric: skill-performance
  - id: atom-3
    title: "Prove it works: unit testing"
    objective: "Write unit tests covering happy path + error cases."
    ksa_refs: [S-write-unit-tests]
    phase: 3
    modalities:
      - { dimension: practice, subtype: "Test Challenge" }
      - { dimension: evaluate, subtype: "Mini-Rubric" }
    deliverable: "Passing test suite with ≥80% coverage of the endpoint"
    rubric: skill-performance
  - id: atom-4
    title: "Requirements changed — adapt & review"
    objective: "Extend the API to a new spec and review a peer's PR."
    ksa_refs: [A-adaptability, A-collaboration, S-build-rest-endpoint]
    phase: 4
    modalities:
      - { dimension: practice,    subtype: "Project Task" }
      - { dimension: collaborate, subtype: "Pair Programming" }
      - { dimension: evaluate,    subtype: "Behavioral Assessment" }
    deliverable: "PR implementing the change + 1 peer review + reflection note"
    rubric: ability-behavioral

capstone:
  title: "Ship a small Tasks API"
  summary: "Design, build, test, and adapt a multi-resource REST API; submit via PR and review a peer."
  integrates_ksa: [K-http-semantics, S-build-rest-endpoint, S-write-unit-tests, A-adaptability, A-collaboration]
  rubric: capstone-5

badge:
  name: "REST API Fundamentals"
  evidence_required: ["capstone", "atom-3", "atom-4"]
  issued_on: verified-evidence            # never AI-only
---
```

---

## 3. Rubric type reference

| `rubric` value | Use for | Heaviest criteria |
| -------------- | ------- | ----------------- |
| `knowledge-mini` | Knowledge atoms | Accuracy, Reasoning |
| `skill-performance` | Skill atoms | Application, Accuracy, Clarity |
| `ability-behavioral` | Ability atoms | Consistency, Self-awareness, Impact on others (≥3 occasions) |
| `capstone-5` | Capstone | Relevance · Application · Problem-Solving · Communication · Collaboration |

The concrete rubric tables are the ones already defined in v1's
[`micro-credential-ada-template.md`](../templates/micro-credential-ada-template.md); v2 just
references them by name and adds the **ability-behavioral** rubric below.

### Ability behavioral rubric (new in v2)

| Criterion | Excellent (3) | Adequate (2) | Needs Improvement (1) |
| --------- | ------------- | ------------ | --------------------- |
| **Consistency across contexts** | Demonstrated in ≥3 varied/real situations | Shown in 2 situations | Shown once or only when prompted |
| **Self-awareness (reflection)** | Insightful reflection naming triggers, choices, growth | Surface reflection | Little/no reflection |
| **Impact on others / outcome** | Visibly improved teamwork/outcome; peers corroborate | Some positive effect | Negligible or negative effect |

---

## 4. Markdown body

After the front matter, include the standard v1 micro-credential sections (title, duration,
target competency, prerequisites, **Bloom objectives — each tagged with its `ksa` id**,
learning atoms, phase planner, capstone, assessment & rubrics, resources, outcomes,
credits). Copy from
[`../templates/micro-credential-ada-template.md`](../templates/micro-credential-ada-template.md)
and add a KSA column to the atom and objective tables, e.g.:

```markdown
## 📘 Learning Objectives (Bloom + KSA)

| Objective | Bloom | KSA | Component | Target |
| --------- | ----- | --- | --------- | ------ |
| Explain HTTP methods & status codes | Understand | 🧠 K | K-http-semantics | L2 |
| Build & test a CRUD endpoint | Create | 🛠️ S | S-build-rest-endpoint | L2 |
| Adapt the API when requirements change | Apply | 🌱 A | A-adaptability | L2 |
```

---

## 5. Validation rules (must pass to publish)

- [ ] `schema: ada-microcredential/v2` present.
- [ ] Every `ksa[]` entry has `id`, `type` ∈ {knowledge,skill,ability}, `target_level` 0–4.
- [ ] ≥1 `skill` **and** ≥1 `ability` present (not Knowledge-only).
- [ ] Every Ability has `assessed_occasions ≥ 3`.
- [ ] Every `atom.ksa_refs` id exists in `ksa[]`.
- [ ] Every `atom.modalities[].dimension` ∈ {read, listen, watch, see, practice, evaluate,
      collaborate} and each `subtype` is a valid leaf from
      [`learning-atom-topology.md`](learning-atom-topology.md), matched to the atom's KSA type.
- [ ] Each atom's `rubric` matches its KSA type (knowledge→mini, skill→performance,
      ability→behavioral).
- [ ] `capstone.integrates_ksa` covers all primary components.
- [ ] `badge.issued_on: verified-evidence`.
- [ ] KSA ids are language-neutral and identical across en/es/pt-br versions.

> Copy this file (front matter + body) to start a new v2 micro-credential. The worked
> examples in [`../examples/`](../examples/) all conform to this schema.
