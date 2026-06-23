# 🧬 ADA v2 — KSA-Driven Applied Digital Apprenticeship

**Status:** Specification (draft v2.0) · **Extends:** [ADA v1 (`README.md`)](../README.md)
· **License:** CC BY-SA 4.0

This is the **core specification** for ADA v2. It defines how the **KSA framework
(Knowledge, Skills, Abilities)** integrates with the existing ADA building blocks
(learning atoms, 4 phases, Bloom alignment, capstones) to produce **job-matched,
Gen AI-authored micro-credentials**.

Read [`ksa-taxonomy.md`](ksa-taxonomy.md) first for definitions. This document is the
"how it all fits together."

---

## 1. What v2 keeps from v1

Nothing valuable is removed. v2 is a **superset**:

- ⚛ **Learning Atoms** — still the smallest unit (`Read · Listen · Watch · Practice ·
  Evaluate · Collaborate`).
- 🔄 **4 Learning Phases** — *hear → see → do → share*.
- 🧱 **Micro-credentials** — 10–30h, 4–8 atoms, capstone, rubric, digital badge.
- 🎯 **Bloom alignment** and **framework anchoring** (SFIA / O\*NET / ESCO / ILO).

> **Backward compatibility:** any v1 micro-credential becomes a valid v2 one by adding
> KSA tags and proficiency targets. No rewrite required.

## 2. What v2 adds

1. **A competency type on everything (KSA).** Every objective and atom is tagged Knowledge,
   Skill, or Ability — and taught/assessed accordingly.
2. **A proficiency level on every competency (0–4).** Makes "ready or not" computable.
3. **A skills map.** A graph of the KSA a learner has vs. what a target job needs.
4. **A job-match score.** The percentage of a role's minimum KSA the learner has evidenced.
5. **A Gen AI authoring loop.** From job posting → target profile → skills map → designed
   atoms → rubrics, with humans validating each gate.

---

## 3. The v2 competency triangle inside ADA

```
                         🌱 ABILITIES (durable / attitudes)
                        develop across the whole journey,
                        proven in Phase 2 & 4 + reflection
                                   ▲
                                   │
                       transfer & │ consistency
                                   │
        🧠 KNOWLEDGE ───────────────────────────────► 🛠️ SKILLS
        (Phase 1: hear)        applied in           (Phase 3: do)
        Read·Listen·Watch                            Practice·labs
```

- **Knowledge** is necessary but not sufficient — it enables Skills.
- **Skills** turn Knowledge into action — proven by artifacts/performance.
- **Abilities** determine whether Knowledge + Skills are applied *consistently and well*
  across changing, real contexts. They are the differentiator employers describe as
  "attitude" and "fit."

A complete competency for a job almost always needs **all three**. v2 forces designers (and
the Gen AI) to ask: *for this role, what K, what S, and what A — at what level?*

---

## 4. KSA across the 4 ADA Phases

Each phase still runs *hear → see → do → share*, but v2 makes its **KSA emphasis**
explicit so designers balance coverage:

| Phase | Confucius | Primary KSA focus | Typical atoms | Evidence produced |
| ----- | --------- | ----------------- | ------------- | ----------------- |
| 🙉 **1 · Self-Guided Introduction** | I hear | **Knowledge** | Read, Listen, Watch + concept check | Concept mastery (quiz/Q&A) |
| 🙈 **2 · Visual Exploration** | I see | **Knowledge → Ability** (modeling, noticing) | Demos, walkthroughs, role-play observation | Annotated analysis, "what good looks like" |
| 🙊 **3 · Applied Practice** | I do | **Skill** | Labs, codelabs, simulations | Built artifact + performance rubric |
| 🐵 **4 · Collaboration & Reflection** | I share | **Ability** (+ Skill transfer) | Peer review, showcase, mentor feedback, reflection | Behavioral evidence + reflection journal |

**Design balance rule:** a micro-credential should not be all-Knowledge. If every atom is
Read/Watch + quiz, it develops only K and will fail at job matching. Each micro-credential
should move the learner on **at least one S and at least one A**, not only K.

---

## 5. The v2 micro-credential lifecycle

```
1. SOURCE the competency        ← job posting / role / framework
2. EXTRACT target KSA profile   ← K, S, A each with target level  (Gen AI + human review)
3. DIFF against learner profile ← what they already evidence
4. BUILD the skills map         ← the gap = what to earn  (graph with prerequisites)
5. DESIGN micro-credentials     ← one per cluster of KSA gaps
6. DESIGN atoms per KSA node    ← teach/assess to the type (K/S/A)
7. ASSESS with typed rubrics    ← knowledge / performance / behavioral
8. ISSUE evidence-based badges  ← update learner profile
9. RE-MATCH                     ← new job-match %  →  loop until job-ready
```

Stages 2, 5, and 6 are where **Gen AI** does the heavy drafting; stages 2, 4, and 7 have
**mandatory human validation gates** (mentor/employer). See
[`genai-authoring-workflow.md`](genai-authoring-workflow.md).

---

## 6. Designing atoms *to the KSA type*

The single most important v2 rule: **teach and assess each atom according to its type.**

### 🧠 Knowledge atoms
- **Lead with:** Read / Listen / Watch.
- **Practice:** retrieval (flashcards, "explain it back", concept maps).
- **Evaluate:** quiz, AI Q&A, accuracy-weighted mini-rubric.
- **Target evidence:** learner can correctly explain and reason about the concept.

### 🛠️ Skill atoms
- **Lead with:** Practice (lab, codelab, simulation) after a short concept primer.
- **Practice:** real reps producing a real artifact; increasing difficulty.
- **Evaluate:** performance rubric on the artifact/observed performance (Accuracy ·
  Application · Clarity); code review / mentor review.
- **Target evidence:** learner produces a working artifact / performs the procedure
  independently at the target level.

### 🌱 Ability atoms
- **Lead with:** authentic, slightly uncomfortable situations (role-play, real
  collaboration, ambiguity) + modeling in Phase 2.
- **Practice:** repeated across *different* contexts; pair with reflection.
- **Evaluate:** behavioral rubric, peer/mentor 360, reflective journal, self-assessment
  with evidence — observed **across multiple occasions**, not one.
- **Target evidence:** learner demonstrates the disposition *consistently* under varied,
  realistic conditions.

> Abilities can't be "completed" in one sitting. v2 recommends threading an Ability across
> **several atoms / weeks** and certifying it from accumulated evidence.

---

## 7. Assessment model (typed rubrics)

v2 keeps v1's rubrics and adds a **typed lens**:

| KSA type | Rubric flavor | Heaviest criteria | Evidence count |
| -------- | ------------- | ----------------- | -------------- |
| Knowledge | Concept/accuracy | Accuracy, Reasoning | 1 (point-in-time ok) |
| Skill | Performance | Application, Accuracy, Clarity | 1–2 artifacts |
| Ability | Behavioral / reflective | Consistency, Self-awareness, Impact on others | ≥3 occasions |

The **capstone** integrates all three: a realistic job task that requires applying
Knowledge, demonstrating Skills, and exhibiting Abilities (collaboration, communication,
adaptability) — scored with the 5-criteria capstone rubric from v1, now explicitly mapped
to KSA coverage.

---

## 8. From competency to credential to job — the matching link

v2's payoff is that competencies are **computable**:

- A **role** = a target KSA profile (each component + minimum level).
- A **learner** = an evidenced KSA profile (each component + achieved level + evidence).
- A **skills map** = the diff (gaps), ordered by prerequisites.
- A **job-match score** = `Σ met-minimums (weighted) / Σ required-minimums`.
- A **micro-credential** closes one or more gaps; earning its badge raises achieved levels
  and the match score.

Full data model and formula: [`skills-map-and-job-matching.md`](skills-map-and-job-matching.md).

---

## 9. Roles & the human-in-the-loop

| Role | Responsibility | Validates |
| ---- | -------------- | --------- |
| **Curriculum designer** | Owns the micro-credential design | Atom quality, KSA balance |
| **Mentor** | Coaches + assesses, esp. Abilities | Behavioral evidence, skill performance |
| **Employer / SME** | Defines the target role | Target KSA profile + minimum levels |
| **Gen AI assistant** | Drafts profiles, maps, atoms, rubrics | (nothing — always reviewed) |
| **Learner** | Produces evidence, reflects | Self-assessment (corroborated) |

**Non-negotiable:** Gen AI **proposes**; a human **validates** target profiles, gap maps,
and any badge issuance. AI-suggested mappings are flagged until confirmed.

---

## 10. Conformance checklist (a micro-credential is "v2-compliant" if…)

- [ ] Anchored to a real role/competency + framework reference (SFIA/O\*NET/ESCO/ILO).
- [ ] Every objective and atom carries a **KSA type** and **target level (0–4)**.
- [ ] Covers **≥1 Skill** and **≥1 Ability**, not Knowledge alone.
- [ ] Each atom is **taught & assessed to its type** (typed rubrics).
- [ ] Abilities are assessed across **≥3 occasions** with reflection.
- [ ] Emits **machine-readable KSA tags** ([schema](micro-credential-v2-schema.md)) so it
      can feed a skills map.
- [ ] Has a capstone integrating K + S + A.
- [ ] Passed a **human validation gate** before badge issuance.
- [ ] (If Gen AI-authored) followed [`genai-authoring-workflow.md`](genai-authoring-workflow.md)
      and logged the review.

---

## 11. Glossary (v2 additions)

- **KSA component** — a single Knowledge, Skill, or Ability item with an ID and level.
- **Target KSA profile** — the set of KSA components (+ minimum levels) a role requires.
- **Learner KSA profile** — the set a learner has evidenced (+ achieved levels).
- **Skills map** — the gap graph between target and learner, ordered by prerequisites.
- **Job-match score** — weighted % of a role's minimums the learner meets.
- **Validation gate** — a required human review step before proceeding/issuing.
