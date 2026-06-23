# 🗺️ Example — End-to-End: From Job Posting to Job-Ready (Skills Map + Match)

This is the **full ADA v2 loop** on a realistic role: a **Junior Frontend Developer**. It
shows how Gen AI turns a job posting into a **target KSA profile**, diffs it against a
learner to build a **skills map**, computes a **job-match score**, prescribes
micro-credentials (covering technical, human, and attitude competencies), and re-scores to
**job-ready**.

Specs used: [`../specs/genai-authoring-workflow.md`](../specs/genai-authoring-workflow.md),
[`../specs/skills-map-and-job-matching.md`](../specs/skills-map-and-job-matching.md),
[`../specs/ksa-taxonomy.md`](../specs/ksa-taxonomy.md).

---

## Step 0 · The job posting (input)

> **Junior Frontend Developer — AcmeApps**
> Build and maintain responsive UIs in React. Turn Figma designs into accessible
> components. Write tests. Collaborate in code review and daily standups. We move fast and
> requirements change — we want someone **adaptable**, **communicative**, and eager to
> learn. JavaScript + HTML/CSS required; Git essential.

---

## Step 1 · Extract Target KSA Profile  🔒 *(Gen AI → human validated)*

The assistant classifies each requirement as K / S / A, assigns a minimum level and weight,
and — importantly — **adds the Abilities the posting implies**. The mentor/employer then
validated levels and confirmed inferred Abilities.

```yaml
role: "Junior Frontend Developer"
source: "AcmeApps posting"
framework_ref: "O*NET 15-1254.00 Web Developers / ESCO: front-end developer"
validated_by: "employer:AcmeApps + mentor:@sancarbar"
requirements:
  - { ref: K-html-css,            type: knowledge, min_level: 2, weight: 3, must_have: true }
  - { ref: K-accessibility-basics, type: knowledge, min_level: 2, weight: 3, must_have: true }
  - { ref: S-javascript,          type: skill,     min_level: 2, weight: 5, must_have: true }
  - { ref: S-react-components,     type: skill,     min_level: 2, weight: 5, must_have: true }
  - { ref: S-figma-to-ui,          type: skill,     min_level: 2, weight: 4, must_have: true }
  - { ref: S-frontend-testing,     type: skill,     min_level: 2, weight: 3, must_have: true }
  - { ref: S-use-git,             type: skill,     min_level: 2, weight: 3, must_have: true }
  - { ref: A-adaptability,        type: ability,   min_level: 2, weight: 3, must_have: false, inferred: true }
  - { ref: A-communication,       type: ability,   min_level: 2, weight: 4, must_have: true }
  - { ref: A-growth-mindset,      type: ability,   min_level: 2, weight: 3, must_have: false, inferred: true }
```

> 🔎 **Human-in-the-loop value:** the posting only said "adaptable, communicative, eager to
> learn." The AI translated those into three concrete, level-rated **Abilities** — and the
> employer confirmed **communication** is actually a `must_have`.

---

## Step 2 · The learner's current profile

From self-assessment + previously earned ADA badges (each level backed by evidence):

```yaml
learner: "ada-learner-042"
evidenced:
  - { ref: K-html-css,            level: 2, evidence: "badge:mc-web-basics", verified: true }
  - { ref: K-accessibility-basics, level: 1, evidence: "self+quiz",          verified: true }
  - { ref: S-javascript,          level: 2, evidence: "badge:mc-js-foundations", verified: true }
  - { ref: S-react-components,     level: 1, evidence: "tutorial project",   verified: true }
  - { ref: S-use-git,             level: 2, evidence: "badge:mc-git-basics", verified: true }
  - { ref: A-communication,       level: 1, evidence: "cohort peer notes",   verified: true }
  # absent (level 0): S-figma-to-ui, S-frontend-testing, A-adaptability, A-growth-mindset
```

---

## Step 3 · Skills Map (the gap graph)  🔒

| Component | Type | Need | Have | Gap | Status | Must-have |
| --------- | ---- | ---- | ---- | --- | ------ | --------- |
| K-html-css | 🧠 K | 2 | 2 | 0 | ✅ met | yes |
| K-accessibility-basics | 🧠 K | 2 | 1 | 1 | 🟡 partial | yes |
| S-javascript | 🛠️ S | 2 | 2 | 0 | ✅ met | yes |
| S-react-components | 🛠️ S | 2 | 1 | 1 | 🟡 partial | yes |
| S-figma-to-ui | 🛠️ S | 2 | 0 | 2 | 🔴 missing | yes |
| S-frontend-testing | 🛠️ S | 2 | 0 | 2 | 🔴 missing | yes |
| S-use-git | 🛠️ S | 2 | 2 | 0 | ✅ met | yes |
| A-adaptability | 🌱 A | 2 | 0 | 2 | 🔴 missing | no |
| A-communication | 🌱 A | 2 | 1 | 1 | 🟡 partial | **yes** |
| A-growth-mindset | 🌱 A | 2 | 0 | 2 | 🔴 missing | no |

```
Prerequisite-ordered "to earn":
 [K-html-css ✅] → [S-react-components 🟡] → [S-figma-to-ui 🔴]
 [K-accessibility-basics 🟡] ─┘
 BLOCKERS (must_have, unmet): S-react-components, S-figma-to-ui, S-frontend-testing,
                              K-accessibility-basics, A-communication
 Boosters (nice-to-have): A-adaptability, A-growth-mindset
```

**Coverage by type:** Knowledge 1/2 · Skill 3/5 · Ability 1/3 → the **Ability** column is
the weakest, exactly the part postings under-specify.

---

## Step 4 · Job-match score (before)

`match = 100 × Σ min(have,need)×weight / Σ need×weight`

| Component | need×w | have×w |
| --------- | ------ | ------ |
| K-html-css | 6 | 6 |
| K-accessibility-basics | 6 | 3 |
| S-javascript | 10 | 10 |
| S-react-components | 10 | 5 |
| S-figma-to-ui | 8 | 0 |
| S-frontend-testing | 6 | 0 |
| S-use-git | 6 | 6 |
| A-adaptability | 6 | 0 |
| A-communication | 8 | 4 |
| A-growth-mindset | 6 | 0 |
| **Σ** | **72** | **34** |

```json
{ "role": "Junior Frontend Developer", "match_score": 47, "job_ready": false,
  "blockers": ["S-react-components","S-figma-to-ui","S-frontend-testing",
               "K-accessibility-basics","A-communication"],
  "coverage": {"knowledge":"1/2","skill":"3/5","ability":"1/3"} }
```

**47% — not job-ready.** Five must-haves unmet (spanning Knowledge, Skills, **and** an
Ability).

---

## Step 5 · Prescribed learning path (micro-credentials per gap)

Gen AI clusters the gaps into a sequenced path mixing **technical, human, and attitude**
development — the core promise of ADA v2:

| # | Micro-credential | Closes (KSA) | Flavor |
| - | ---------------- | ------------ | ------ |
| 1 | **Accessible UI with React** | K-accessibility-basics →2, S-react-components →2 | 🛠️ technical + 🧠 knowledge |
| 2 | **From Figma to Components** | S-figma-to-ui →2 | 🛠️ technical |
| 3 | **Frontend Testing Essentials** | S-frontend-testing →2 | 🛠️ technical |
| 4 | **[Feedback That Helps](ksa-human-skill-feedback.md)** | A-communication →2 | 🤝 human skill |
| 5 | **[Thriving in Change](ksa-attitude-adaptability.md)** | A-adaptability →2, A-growth-mindset →2 | 🌱 attitude |

Note MC #4 and #5 **reuse the worked examples in this repo** — the same KSA components flow
straight into the job match.

---

## Step 6 · Job-match score (after completing the path)

Each earned badge updates the learner profile to the target levels. New `have×weight`:

| Component | need×w | have×w (after) |
| --------- | ------ | -------------- |
| K-html-css | 6 | 6 |
| K-accessibility-basics | 6 | 6 |
| S-javascript | 10 | 10 |
| S-react-components | 10 | 10 |
| S-figma-to-ui | 8 | 8 |
| S-frontend-testing | 6 | 6 |
| S-use-git | 6 | 6 |
| A-adaptability | 6 | 6 |
| A-communication | 8 | 8 |
| A-growth-mindset | 6 | 6 |
| **Σ** | **72** | **72** |

```json
{ "role": "Junior Frontend Developer", "match_score": 100, "job_ready": true,
  "blockers": [], "coverage": {"knowledge":"2/2","skill":"5/5","ability":"3/3"} }
```

**100% and job-ready** — all must-haves met across all three KSA types.

> A learner short on time could stop after MC #1–#4: that clears every **must_have**
> (A-adaptability and A-growth-mindset are not blocking). Recompute: have = 72 − 6 (adapt)
> − 6 (growth) = 60 → 60/72 ≈ **83%**, just under the 85% threshold but **job-eligible**
> since no blockers remain. The two attitude boosters then take them to 100% and stronger
> standing.

---

## Step 7 · What the learner walks away with

- 🏅 **5 verified badges** mapped to real KSA components.
- 🗂️ A **portfolio** (React app, Figma-built components, test suite, a recorded feedback
  conversation, a growth journal / pivot project).
- 📊 A shareable **match report** showing 100% against the target role, broken down by
  Knowledge, Skills, and Abilities.
- 🔁 A reusable profile that can be **re-matched against other roles** instantly.

---

## The big picture

```
 Posting → [AI extract+human validate] → Target KSA Profile
         → [diff with learner] → Skills Map + 47% match (not ready)
         → [design path: technical + human + attitude micro-credentials]
         → [learn · produce evidence · earn badges] → profile updated
         → [re-match] → 100% match → JOB-READY
```

This is ADA v2: **a clear, KSA-driven framework that uses Gen AI to design micro-credentials
and a skills map that tells a learner exactly what to earn to meet a job's minimum bar —
across knowledge, technical skills, human skills, and attitudes.**
