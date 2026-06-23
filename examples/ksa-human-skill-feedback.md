# 🤝 Example — Human Skill: Giving & Receiving Feedback (KSA)

**KSA flavor demonstrated:** a **human/durable Skill** (the technique of structuring
feedback) explicitly paired with an **Ability** (empathetic, psychologically-safe
communication) and grounded in **Knowledge** (feedback models).

This example shows that "soft" competencies decompose with the **same KSA rigor** as
technical ones — and why human competencies usually need **both** a Skill layer (the
repeatable technique) **and** an Ability layer (the disposition shown across situations).

Conforms to [`../specs/micro-credential-v2-schema.md`](../specs/micro-credential-v2-schema.md).

---

## YAML front matter

```yaml
---
schema: ada-microcredential/v2
id: mc-feedback-conversations
title: "Feedback That Helps: Giving & Receiving Feedback"
language: en
duration_hours: 12
status: published
license: CC-BY-SA-4.0
mentors: ["@sancarbar"]

target_roles:
  - role: "Team Lead / Senior Individual Contributor"
    framework_ref: "ESCO: transversal skills – communication, teamwork / O*NET: Social Skills"

ksa:
  - { id: K-feedback-models, type: knowledge, label: "Feedback models (SBI, radical candor, growth feedback)", target_level: 2, bloom: understand }
  - { id: S-structure-feedback, type: skill, label: "Structure a feedback conversation (SBI: Situation-Behavior-Impact)", target_level: 2, bloom: apply, primary: true, prerequisites: [K-feedback-models] }
  - { id: S-receive-feedback, type: skill, label: "Receive feedback without defensiveness; ask clarifying questions", target_level: 2, bloom: apply }
  - { id: A-empathetic-communication, type: ability, label: "Communicate with empathy & create psychological safety", target_level: 2, affective_stage: value, assessed_occasions: 3 }

atoms:
  - { id: atom-1, title: "Why feedback fails — and the models that work", ksa_refs: [K-feedback-models], phase: 1, formats: [read, listen, evaluate], rubric: knowledge-mini }
  - { id: atom-2, title: "Watch good & bad feedback", ksa_refs: [K-feedback-models, A-empathetic-communication], phase: 2, formats: [watch, evaluate], rubric: knowledge-mini }
  - { id: atom-3, title: "Role-play: give SBI feedback", ksa_refs: [S-structure-feedback, A-empathetic-communication], phase: 3, formats: [practice, collaborate, evaluate], rubric: ability-behavioral }
  - { id: atom-4, title: "Receive feedback & reflect", ksa_refs: [S-receive-feedback, A-empathetic-communication], phase: 4, formats: [practice, collaborate, evaluate], rubric: ability-behavioral }

capstone:
  title: "Run a real feedback conversation"
  integrates_ksa: [K-feedback-models, S-structure-feedback, S-receive-feedback, A-empathetic-communication]
  rubric: capstone-5

badge:
  name: "Feedback That Helps"
  evidence_required: ["atom-3", "atom-4", "capstone"]
  issued_on: verified-evidence
---
```

---

## 🎯 Target Job Competency
Give and receive **actionable, respectful feedback** — a transversal competency for any
leadership or senior IC role (ESCO transversal skills: communication, teamwork).

## 🧬 KSA breakdown — and the Skill ↔ Ability distinction

| KSA | Component | Why this type | Target |
| --- | --------- | ------------- | ------ |
| 🧠 Knowledge | Feedback models (SBI, growth feedback) | Concepts you recall & reason with | L2 |
| 🛠️ Skill | Structure a feedback conversation (SBI) | A **repeatable technique** that improves with reps | L2 |
| 🛠️ Skill | Receive feedback constructively | Also a practiced procedure | L2 |
| 🌱 Ability | Empathetic communication / psychological safety | A **disposition** shown consistently across people & moments | L2 |

> **Key teaching point:** the *technique* of SBI is a **Skill** (learnable in reps). Doing
> it with genuine empathy that makes others feel safe is an **Ability** (a disposition
> proven across many conversations). v2 develops and assesses **both**.

## 📘 Learning Objectives (Bloom + KSA)

| Objective | Bloom | KSA | Component | Target |
| --------- | ----- | --- | --------- | ------ |
| Compare common feedback models | Understand | 🧠 K | K-feedback-models | L2 |
| Deliver feedback using SBI | Apply | 🛠️ S | S-structure-feedback | L2 |
| Receive feedback without defensiveness | Apply | 🛠️ S | S-receive-feedback | L2 |
| Communicate with empathy / safety | Value | 🌱 A | A-empathetic-communication | L2 |

---

## ⚛ Learning Atoms — *taught & assessed to type*

> Modalities below are chosen from the [Learning Atom Topology](../specs/learning-atom-topology.md):
> 📖 *Article* · 🎧 *Podcast* · 🎬 *paired clips* · 🧪 *Role-Play* · 🤝 *Peer 360* · ✅ *Behavioral Assessment*.

### Atom 1 · "Why feedback fails — and what works" — 🧠 Knowledge *(Phase 1)*
- **Read:** SBI model + growth-feedback overview. **Listen:** podcast on candor vs. kindness.
- **Evaluate:** concept check — classify statements as observation vs. judgment.
- **Evidence:** ≥80% quiz → K-feedback-models **L2**. **Rubric:** `knowledge-mini`.

### Atom 2 · "Watch good & bad feedback" — 🧠 K → 🌱 A modeling *(Phase 2: see)*
- **Watch:** paired clips of effective vs. damaging feedback.
- **Evaluate:** annotate what created (or destroyed) psychological safety.
- **Purpose:** builds the mental model of what the Ability *looks like* before practicing it.

### Atom 3 · "Role-play: give SBI feedback" — 🛠️ Skill + 🌱 Ability *(Phase 3: do)*
- **Practice:** role-play giving feedback to a peer on a real-ish scenario (occasion 1),
  then a second, different scenario (occasion 2).
- **Collaborate:** peers + mentor observe and coach.
- **Evaluate:** behavioral rubric on **both** the SBI structure (Skill) and the empathy /
  safety created (Ability).
- **Evidence:** structured, empathetic delivery in 2 scenarios → S-structure-feedback **L2**
  + partial A evidence. **Rubric:** `ability-behavioral`.

### Atom 4 · "Receive feedback & reflect" — 🛠️ Skill + 🌱 Ability *(Phase 4: share)*
- **Practice:** receive live feedback; respond with clarifying questions, no defensiveness.
- **Collaborate:** 360 mini-survey from 2 peers + mentor (occasion 3).
- **Reflect:** journal on your default reaction and how you regulated it.
- **Evidence:** corroborated calm, curious reception → S-receive-feedback **L2**; combined
  with Atoms 2–3 → A-empathetic-communication **L2** (3 occasions met).

---

## 🔍 Phase planner

| Phase | Atom(s) | KSA focus | Activity | Assessment |
| ----- | ------- | --------- | -------- | ---------- |
| 🙉 1 | Atom 1 | 🧠 K | read/listen + quiz | knowledge-mini |
| 🙈 2 | Atom 2 | 🧠 K → 🌱 A | annotate clips | formative |
| 🙊 3 | Atom 3 | 🛠️ S + 🌱 A | role-play ×2 | behavioral |
| 🐵 4 | Atom 4 | 🛠️ S + 🌱 A | receive + 360 + reflect | behavioral + 360 |

---

## 🚀 Capstone — "Run a real feedback conversation"
Conduct an actual (or high-fidelity simulated) feedback conversation, recorded or observed,
then receive feedback on your feedback. Submit a reflection. Scored with the 5-criteria
capstone rubric:

| Capstone criterion | Evidences |
| ------------------ | --------- |
| Relevance | K-feedback-models |
| Application of Skills | S-structure-feedback, S-receive-feedback |
| Problem-Solving & Creativity | adapting tone to the person/situation |
| Clarity & Communication | A-empathetic-communication |
| Collaboration & Reflection | 360 + reflection journal |

### 📋 Assessment Rubric (capstone-5)

Five criteria across four proficiency bands, weighted to **100 points** (pass ≥ 70%, at least
*Developing* on every criterion; mentor-verified).

| Criteria | Excellent (100–90%) | Competent (89–80%) | Developing (79–70%) | Initial (69% or less) | Weight |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Relevance (competency alignment)** | Conversation is a real, job-relevant feedback case, framed accurately. | Relevant; framing mostly accurate. | Loosely relevant; framing partly off. | Off-target or inaccurate framing. | **20 pts** |
| **Application of Skills** | SBI structure + skilled receiving used cleanly. | Both used adequately, minor gaps. | Inconsistent or partial use. | Minimal or incorrect application. | **25 pts** |
| **Problem-Solving & Creativity** | Adapts tone to the person/situation insightfully. | Sound, conventional adaptation. | Some adaptation; uneven. | Rigid; no adaptation. | **20 pts** |
| **Clarity & Communication** | Empathetic, clear, well-structured delivery + reflection. | Generally clear. | Uneven clarity. | Unclear or missing. | **15 pts** |
| **Collaboration & Reflection** | Strong 360 engagement + insightful reflection journal. | Moderate engagement + reflection. | Minimal. | Missing. | **20 pts** |
| **TOTAL** | | | | | **100 pts** |

## 🌱 Why the Ability needs ≥3 occasions
A single good conversation could be luck. v2 certifies `A-empathetic-communication` only
after it shows up across **Atom 2 (recognize), Atom 3 (×2 role-plays), Atom 4 (live + 360)**
— consistency across contexts is the definition of an Ability.

## 🏅 Badge → skills map
Sets `K-feedback-models=2`, `S-structure-feedback=2`, `S-receive-feedback=2`,
`A-empathetic-communication=2` — the human-skill cluster many leadership roles list as a
`must_have` Ability that postings rarely teach.
