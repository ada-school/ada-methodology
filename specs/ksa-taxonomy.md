# 🧩 KSA Taxonomy — Knowledge, Skills, Abilities

The **KSA framework** is the competency spine of ADA v2. It gives every learning objective
a *type*, so it can be taught, practiced, and assessed in the way that actually develops it
— and so it can be matched against a job's requirements.

KSA originates in occupational and human-resources practice (e.g. O\*NET descriptors,
job-analysis standards) and pairs naturally with ADA's existing Bloom alignment.

---

## 1. The three types

### 🧠 Knowledge — the *know-what* and *know-why*

Theoretical, factual, and conceptual understanding a person can recall and reason with.
It is **cognitive** and largely acquired through study and exposure.

- *Examples:* HTTP status code semantics; principles of color theory; what psychological
  safety is; the stages of a sales funnel; how diffusion models generate images.
- *Develops through:* Read · Listen · Watch atoms; case studies; explanation.
- *Assessed with:* quizzes, concept checks, oral/AI Q&A, "explain it back" prompts.
- *Bloom home:* Remember, Understand (extends into Analyze/Evaluate).

### 🛠️ Skills — the *know-how*

Procedural proficiencies developed through **deliberate, repeated practice**. Observable
and improvable; can be **technical/hard** (build a REST API, run a regression) or
**human/applied** (facilitate a retro, give structured feedback).

- *Examples:* writing a Flask endpoint; building a dashboard; running a 1:1; structuring a
  feedback conversation; pitching to a stakeholder.
- *Develops through:* Practice atoms, labs, codelabs, simulations, role-play, reps.
- *Assessed with:* performance tasks, rubrics on a produced artifact or observed
  performance, code review, capstone.
- *Bloom home:* Apply, Analyze, Create.

### 🌱 Abilities — the *can-do* / *will-do* (durable capacities & attitudes)

Enduring personal capacities and dispositions that shape *how consistently and how well*
someone applies knowledge and skills across changing contexts. This is where **attitudes
and human/durable qualities** live: adaptability, resilience, curiosity, collaboration,
integrity, growth mindset, attention to detail.

- *Examples:* adapts approach when requirements change; persists through ambiguity;
  collaborates across disciplines; takes ownership; communicates with empathy.
- *Develops through:* repeated authentic practice + reflection + feedback over time
  (Collaborate atoms, Phase 4, mentorship, real/realistic stakes).
- *Assessed with:* behavioral rubrics, reflective journals, peer/mentor 360 feedback,
  observation across multiple situations, self-assessment + evidence.
- *Bloom home:* spans all levels; best paired with the **affective domain**
  (Receive → Respond → Value → Organize → Internalize).

> **Skill vs. Ability — the practical test:** if it improves mainly through *reps and
> procedure*, treat it as a **Skill**. If it is a *disposition expressed consistently
> across situations* (and shows up as "attitude" in a job posting), treat it as an
> **Ability**. Many human competencies have both a Skill layer (the technique) and an
> Ability layer (the disposition) — model both when it matters (see the feedback example).

---

## 2. Side-by-side

| Dimension | 🧠 Knowledge | 🛠️ Skill | 🌱 Ability |
| --------- | ----------- | -------- | --------- |
| Question | Know-what / know-why | Know-how | Can-do / will-do |
| Nature | Cognitive | Procedural | Dispositional / durable |
| Acquired by | Study, exposure | Deliberate practice | Practice + reflection over time |
| Time to develop | Short–medium | Medium | Long, continuous |
| Primary atom formats | Read, Listen, Watch | Practice | Collaborate + Practice + Reflect |
| Evidence | Correct recall/explanation | Artifact / performance | Consistent behavior across contexts |
| Assessment | Quiz, concept check | Performance rubric | Behavioral rubric, 360, reflection |
| Bloom | Remember, Understand | Apply, Analyze, Create | All + Affective domain |
| Volatility | Higher (facts change) | Medium | Low (transfers across roles) |

---

## 3. How to classify a competency (decision flow)

```
Is it information you must recall or reason with?              → KNOWLEDGE (K)
   ↓ no
Is it a procedure that gets better with reps / produces an artifact? → SKILL (S)
   ↓ no
Is it a disposition/attitude shown consistently across situations?   → ABILITY (A)
```

Tie-breakers:
- A job posting line that reads as a **tool, language, method, or task** → usually **S**
  (with a **K** prerequisite).
- A line that reads as an **adjective about the person** ("adaptable", "collaborative",
  "detail-oriented", "self-driven") → **A**.
- A line that reads as a **concept/standard to understand** → **K**.

---

## 4. Proficiency scale (shared, 0–4)

Every KSA component carries a target **proficiency level**. Use one scale across all three
types so gaps are computable (see `skills-map-and-job-matching.md`). Aligned loosely with
SFIA levels and Dreyfus stages.

| Level | Label | Knowledge looks like | Skill looks like | Ability looks like |
| ----- | ----- | -------------------- | ---------------- | ------------------ |
| **0** | None | No exposure | Cannot perform | Not yet observed |
| **1** | Aware | Can recognize/recall basics | Performs with full guidance | Shows it occasionally, prompted |
| **2** | Working | Explains and relates concepts | Performs routine cases independently | Shows it reliably in familiar contexts |
| **3** | Proficient | Reasons about edge cases/trade-offs | Handles novel/complex cases, mentors others | Shows it under pressure / new contexts |
| **4** | Expert | Synthesizes, teaches, sets standards | Sets best practice, optimizes | Role-models and develops it in others |

**Job-readiness rule of thumb:** most entry-level roles require **L2 (Working)** on core
KSA and **L1 (Aware)** on adjacent KSA. v2 makes this explicit per role.

---

## 5. Mapping KSA → ADA building blocks

| ADA element | Knowledge | Skill | Ability |
| ----------- | --------- | ----- | ------- |
| **Atom formats** | Read, Listen, Watch | Practice | Collaborate (+ Practice, + Reflect) |
| **Phase emphasis** | Phase 1 (Self-Guided) | Phase 3 (Applied Practice) | Phases 2 & 4 (Visual + Collaboration/Reflection) |
| **Deliverable** | Concept artifact / explanation | Built artifact / performance | Reflection + behavioral evidence |
| **Rubric type** | Accuracy-weighted | Application-weighted | Behavioral / 360 / reflection-weighted |

Every **learning atom in v2 declares its KSA type(s)** and the target level it moves the
learner toward. A single atom may touch more than one type (e.g. a feedback role-play
builds the *skill* of structuring feedback **and** the *ability* of empathetic
communication) — tag the **primary** type and list secondaries.

---

## 6. KSA tag format (used in atoms & micro-credentials)

```yaml
ksa:
  - id: K-http-semantics
    type: knowledge
    label: "HTTP request/response semantics"
    target_level: 2          # 0–4 scale above
    framework_ref: "SFIA:PROG / O*NET:15-1254.00"
  - id: S-build-rest-endpoint
    type: skill
    label: "Build & test a REST endpoint"
    target_level: 2
    primary: true
  - id: A-adaptability
    type: ability
    label: "Adaptability under changing requirements"
    target_level: 2
    affective_stage: respond   # receive|respond|value|organize|internalize
```

See [`micro-credential-v2-schema.md`](micro-credential-v2-schema.md) for the full schema
and [`skills-map-and-job-matching.md`](skills-map-and-job-matching.md) for how these IDs
feed the matchable skills graph.
