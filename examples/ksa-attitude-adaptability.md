# 🌱 Example — Attitude / Ability: Adaptability & Growth Mindset (KSA)

**KSA flavor demonstrated:** a pure **Ability** (an attitude / durable disposition) — the
hardest type to teach and assess, and the one job postings most often demand ("adaptable",
"thrives in ambiguity", "growth mindset") yet rarely develop intentionally.

This example shows how v2 makes an *attitude* trainable and certifiable by: modeling it,
threading it across **multiple authentic occasions**, and assessing it with a **behavioral
rubric + reflection + 360**, never a quiz.

Conforms to [`../specs/micro-credential-v2-schema.md`](../specs/micro-credential-v2-schema.md).

---

## YAML front matter

```yaml
---
schema: ada-microcredential/v2
id: mc-adaptability-growth-mindset
title: "Thriving in Change: Adaptability & Growth Mindset"
language: en
duration_hours: 14
status: published
license: CC-BY-SA-4.0
mentors: ["@sancarbar"]

target_roles:
  - role: "Any role in a fast-changing digital team"
    framework_ref: "O*NET Work Styles: Adaptability/Flexibility, Persistence / ESCO: transversal attitudes"

ksa:
  - { id: K-mindset-science, type: knowledge, label: "Fixed vs. growth mindset; basics of self-regulation", target_level: 1, bloom: understand }
  - { id: S-reframing-technique, type: skill, label: "Apply a reframing/learning-loop technique under setback", target_level: 2, bloom: apply }
  - { id: A-adaptability, type: ability, label: "Adapt approach & stay effective amid change/ambiguity", target_level: 2, primary: true, affective_stage: organize, assessed_occasions: 4 }
  - { id: A-growth-mindset, type: ability, label: "Treat failure as learning; seek challenge & feedback", target_level: 2, affective_stage: value, assessed_occasions: 3 }

atoms:
  - { id: atom-1, title: "The science of mindset", ksa_refs: [K-mindset-science], phase: 1, formats: [read, watch, evaluate], rubric: knowledge-mini }
  - { id: atom-2, title: "Spot the mindset", ksa_refs: [K-mindset-science, A-growth-mindset], phase: 2, formats: [watch, evaluate], rubric: knowledge-mini }
  - { id: atom-3, title: "The curveball lab", ksa_refs: [A-adaptability, S-reframing-technique], phase: 3, formats: [practice, collaborate, evaluate], rubric: ability-behavioral }
  - { id: atom-4, title: "Failure résumé & growth journal", ksa_refs: [A-growth-mindset, A-adaptability], phase: 4, formats: [practice, collaborate, evaluate], rubric: ability-behavioral }

capstone:
  title: "The pivot challenge"
  integrates_ksa: [K-mindset-science, S-reframing-technique, A-adaptability, A-growth-mindset]
  rubric: capstone-5

badge:
  name: "Thriving in Change"
  evidence_required: ["atom-3", "atom-4", "capstone"]
  issued_on: verified-evidence
---
```

---

## 🎯 Target Job Competency
Stay effective and keep learning when **goals, tools, or requirements change** — listed in
postings as *adaptability, flexibility, resilience, growth mindset* (O\*NET Work Styles;
ESCO transversal attitudes).

## 🧬 KSA breakdown — an attitude, modeled as Abilities

| KSA | Component | Why this type | Target |
| --- | --------- | ------------- | ------ |
| 🧠 Knowledge | Fixed vs. growth mindset; self-regulation basics | Concepts to understand (small enabling layer) | L1 |
| 🛠️ Skill | A reframing / learning-loop technique | A *teachable move* you can practice in reps | L2 |
| 🌱 Ability | Adaptability amid change | A disposition shown across many situations | L2 |
| 🌱 Ability | Growth mindset (failure = learning) | A disposition / attitude shown over time | L2 |

> **Why two Abilities + one Skill:** an attitude isn't taught by lecturing it. v2 gives the
> learner a small **Knowledge** base, a concrete **Skill** (a reframing move they can
> actually do), and then builds the **Abilities** through repeated, real exposure to
> change — because dispositions are proven by *behavior across contexts*, not by a test.

## 📘 Learning Objectives (Bloom + Affective + KSA)

| Objective | Bloom / Affective | KSA | Component | Target |
| --------- | ----------------- | --- | --------- | ------ |
| Explain fixed vs. growth mindset | Understand | 🧠 K | K-mindset-science | L1 |
| Apply a reframing technique to a setback | Apply | 🛠️ S | S-reframing-technique | L2 |
| Adapt approach when conditions change | Organize (affective) | 🌱 A | A-adaptability | L2 |
| Treat failure as learning; seek challenge | Value (affective) | 🌱 A | A-growth-mindset | L2 |

---

## ⚛ Learning Atoms — *attitude-appropriate design*

> Modalities below are chosen from the [Learning Atom Topology](../specs/learning-atom-topology.md):
> 🖼️ *Mental Model* · 🎬 *case clips* · 🧪 *Simulation / Role-Play* · 📖 *Journal* · 🤝 *Study Group* · ✅ *Behavioral Assessment*.

### Atom 1 · "The science of mindset" — 🧠 Knowledge *(Phase 1)*
- **Read/Watch:** growth-mindset overview; what self-regulation is.
- **Evaluate:** quick concept check. **Evidence:** K-mindset-science **L1**.
- *(Knowledge here is intentionally light — L1 — it only enables the Abilities.)*

### Atom 2 · "Spot the mindset" — 🧠 K → 🌱 A modeling *(Phase 2: see)*
- **Watch:** clips/cases of people facing setbacks with fixed vs. growth responses.
- **Evaluate:** identify the language and behaviors of each; predict outcomes.
- **Purpose:** lets learners *recognize* the target Ability before being asked to live it.

### Atom 3 · "The curveball lab" — 🌱 Ability + 🛠️ Skill *(Phase 3: do)*
- **Practice:** mid-task, the brief **changes twice** (new constraint, then a removed
  resource). Learner replans using the reframing technique. *(occasions 1 & 2)*
- **Collaborate:** debrief with peers; mentor observes how the learner responded to change.
- **Evaluate:** behavioral rubric on *adaptation* (did they re-plan vs. freeze?) + correct
  use of the reframing move.
- **Evidence:** effective response to 2 changes → S-reframing-technique **L2**; partial
  A-adaptability evidence.

### Atom 4 · "Failure résumé & growth journal" — 🌱 Ability *(Phase 4: share)*
- **Practice:** write a *failure résumé* (a real setback + what was learned); set a
  stretch goal and pursue feedback on it. *(occasion 3)*
- **Collaborate:** share with the cohort; give/receive supportive challenge.
- **Reflect:** ongoing growth journal across the 2–3 weeks *(occasion 4 — sustained)*.
- **Evaluate:** behavioral rubric + peer/mentor 360 on sustained behavior.
- **Evidence:** A-growth-mindset **L2** (3 occasions) and A-adaptability **L2** (4 occasions).

---

## 🔍 Phase planner

| Phase | Atom(s) | KSA focus | Activity | Assessment |
| ----- | ------- | --------- | -------- | ---------- |
| 🙉 1 | Atom 1 | 🧠 K | mindset readings/video | knowledge-mini |
| 🙈 2 | Atom 2 | 🧠 K → 🌱 A | analyze case clips | formative |
| 🙊 3 | Atom 3 | 🌱 A + 🛠️ S | curveball lab (change ×2) | behavioral |
| 🐵 4 | Atom 4 | 🌱 A | failure résumé + journal + 360 | behavioral + 360 |

---

## 📊 Behavioral rubric (the right tool for an attitude)

| Criterion | Excellent (3) | Adequate (2) | Needs Improvement (1) |
| --------- | ------------- | ------------ | --------------------- |
| **Consistency across contexts** | Adapted effectively across all 4 occasions | Adapted in 2–3 | Froze/resisted; only when pushed |
| **Self-awareness (reflection)** | Names triggers, choices, and growth with insight | Some reflection | Minimal/none |
| **Response to setback/feedback** | Reframes as learning, seeks the challenge | Accepts but passive | Defensive or avoidant |

> An attitude can't be certified from one moment or a quiz. The rubric explicitly requires
> evidence **across occasions** — that's what separates an Ability from a Skill.

## 🚀 Capstone — "The pivot challenge"
A multi-day project whose goal **pivots partway through**. Learners must re-scope, keep the
team moving, document what they changed and why, and reflect on how they handled it.
Capstone criteria map to KSA:

| Capstone criterion | Evidences |
| ------------------ | --------- |
| Relevance | adapting to a realistic pivot |
| Application of Skills | S-reframing-technique |
| Problem-Solving & Creativity | A-adaptability |
| Clarity & Communication | reflection + change log |
| Collaboration & Reflection | A-growth-mindset + peer 360 |

### 📋 Assessment Rubric (capstone-5)

Five criteria across four proficiency bands, weighted to **100 points** (pass ≥ 70%, at least
*Developing* on every criterion; mentor-verified). Because this certifies an **Ability**, pair it
with the behavioral rubric across occasions above.

| Criteria | Excellent (100–90%) | Competent (89–80%) | Developing (79–70%) | Initial (69% or less) | Weight |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Relevance (competency alignment)** | The pivot is a realistic, job-relevant stretch; framing accurate. | Relevant; framing mostly accurate. | Loosely relevant; framing partly off. | Off-target or inaccurate. | **20 pts** |
| **Application of Skills** | Reframing technique used skillfully to re-scope. | Used adequately, minor gaps. | Attempted but inconsistent. | Largely absent or misapplied. | **25 pts** |
| **Problem-Solving & Creativity** | Re-plans calmly into a smart new path. | Sound, conventional re-plan. | Some re-planning; stalls at points. | Freezes; no adaptation. | **20 pts** |
| **Clarity & Communication** | Clear change log + honest, structured reflection. | Generally clear. | Uneven clarity. | Unclear or missing. | **15 pts** |
| **Collaboration & Reflection** | Strong peer 360 + deeply insightful reflection. | Moderate engagement + reflection. | Minimal. | Missing. | **20 pts** |
| **TOTAL** | | | | | **100 pts** |

## 🏅 Badge → skills map
Sets `A-adaptability=2` and `A-growth-mindset=2` — exactly the durable Abilities that
employers list as `must_have` "attitude/fit" and that a Knowledge-only course can never
certify. This badge is what closes the **Ability** gaps in a job-match skills map.
