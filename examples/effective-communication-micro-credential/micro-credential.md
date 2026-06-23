# 🎓 Micro-Credential — Effective Communication: Listen, Structure & Connect

The full specification for this micro-credential. It conforms to
[`../../specs/micro-credential-v2-schema.md`](../../specs/micro-credential-v2-schema.md).

---

## YAML front matter

```yaml
schema: ada-microcredential/v2
id: mc-effective-communication
title: "Effective Communication: Listen, Structure & Connect"
language: en
duration_hours: 12
level: beginner
status: published
license: CC-BY-SA-4.0
mentors: ["@sancarbar"]

target_roles:
  - role: "Any role — communication is a transversal, near-universal job requirement (ICs, leads, client-facing, technical)"
    framework_ref: >
      O*NET basic skills: 2.A.1.b Active Listening, 2.A.1.d Speaking, 2.A.1.c Writing ·
      O*NET social skills: 2.B.1.a Social Perceptiveness, 2.B.1.e Persuasion ·
      ESCO transversal: "communicate effectively", "use active listening techniques"

ksa:
  - { id: K-comm-model,       type: knowledge, label: "How communication works: sender→message→channel→receiver→feedback; noise & barriers", target_level: 2, bloom: understand }
  - { id: K-audience-channel, type: knowledge, label: "Audience analysis and channel selection (sync/async, media richness)", target_level: 2, bloom: understand }
  - { id: S-active-listening, type: skill,     label: "Listen actively: attend, paraphrase, ask clarifying questions, check understanding", target_level: 2, bloom: apply, primary: true }
  - { id: S-structure-message, type: skill,    label: "Structure a clear message (BLUF, SBI, Pyramid Principle) in writing and speech", target_level: 2, bloom: apply, primary: true }
  - { id: S-feedback-difficult, type: skill,   label: "Give/receive feedback and navigate difficult conversations (SBI + nonviolent communication)", target_level: 2, bloom: apply }
  - { id: A-empathy,          type: ability,   label: "Empathy & audience-awareness: read the other person and adapt", target_level: 2, affective_stage: value, assessed_occasions: 3 }
  - { id: A-assertiveness,    type: ability,   label: "Assertive, respectful expression under pressure (clear, calm, honest)", target_level: 2, affective_stage: respond, assessed_occasions: 3 }

atoms:
  - { id: atom-1, title: "How communication works", ksa_refs: [K-comm-model], phase: 1, modalities: [{dimension: read, subtype: Article}, {dimension: watch, subtype: Video Explainer}, {dimension: see, subtype: Diagram}, {dimension: evaluate, subtype: Pop Quiz}], rubric: knowledge-mini }
  - { id: atom-2, title: "Audience & channel", ksa_refs: [K-audience-channel], phase: 1, modalities: [{dimension: read, subtype: Article}, {dimension: see, subtype: Framework}, {dimension: practice, subtype: Worksheet / Exercise}, {dimension: evaluate, subtype: Pop Quiz}], rubric: knowledge-mini }
  - { id: atom-3, title: "Active listening", ksa_refs: [S-active-listening, A-empathy], phase: 2, modalities: [{dimension: watch, subtype: Video Explainer}, {dimension: see, subtype: Mental Model}, {dimension: practice, subtype: Role-Play}, {dimension: collaborate, subtype: Pair Programming}, {dimension: evaluate, subtype: Mini-Rubric}], rubric: skill }
  - { id: atom-4, title: "Structure your message (BLUF · SBI · Pyramid)", ksa_refs: [S-structure-message], phase: 3, modalities: [{dimension: read, subtype: Technical Article}, {dimension: practice, subtype: Worksheet / Exercise}, {dimension: practice, subtype: AI Prompt Question}, {dimension: evaluate, subtype: Performance Task}], rubric: skill }
  - { id: atom-5, title: "Feedback & difficult conversations", ksa_refs: [S-feedback-difficult, A-assertiveness, A-empathy], phase: 3, modalities: [{dimension: read, subtype: Case Study}, {dimension: practice, subtype: Role-Play}, {dimension: practice, subtype: Simulation}, {dimension: evaluate, subtype: Behavioral Assessment}], rubric: behavioral }
  - { id: atom-6, title: "Communication capstone + peer review", ksa_refs: [S-active-listening, S-structure-message, S-feedback-difficult, A-empathy, A-assertiveness], phase: 4, modalities: [{dimension: practice, subtype: Performance Task}, {dimension: collaborate, subtype: Showcase / Demo Day}, {dimension: collaborate, subtype: Async Peer Review}, {dimension: evaluate, subtype: Capstone Project}], rubric: capstone-5 }

capstone:
  title: "Deliver a clear message and lead a real conversation, then reflect"
  integrates_ksa: [K-comm-model, K-audience-channel, S-active-listening, S-structure-message, S-feedback-difficult, A-empathy, A-assertiveness]
  rubric: capstone-5

badge:
  name: "Effective Communicator"
  evidence_required: ["atom-3", "atom-4", "atom-5", "capstone"]
  issued_on: verified-evidence
```

---

## 🎯 Target job competency

**Communicate effectively** at work: listen so people feel heard, say/write things so people
understand and act, and handle feedback and tension without damaging the relationship. It is the
single most common line in job postings — *"excellent communication skills", "stakeholder
communication", "active listening", "clear written communication".* Mapped to **O\*NET** basic skills
(Active Listening, Speaking, Writing) and social skills (Social Perceptiveness, Persuasion), and
**ESCO** transversal communication skills.

## 🧬 KSA breakdown — a human skill, taught the right way

| KSA | Component | Why this type | Target |
| --- | --------- | ------------- | ------ |
| 🧠 Knowledge | How communication works (model, noise) | A small mental model that explains *why* messages fail | L2 |
| 🧠 Knowledge | Audience & channel | Prevents the "right message, wrong channel/audience" failure | L2 |
| 🛠️ Skill | Active listening | A trainable technique (paraphrase, clarify, check) | **L2** |
| 🛠️ Skill | Structure a clear message | BLUF/SBI/Pyramid — practiced in writing & speech | **L2** |
| 🛠️ Skill | Feedback & difficult conversations | A procedure for high-stakes moments | L2 |
| 🌱 Ability | Empathy & audience-awareness | A disposition shown across situations, over time | L2 |
| 🌱 Ability | Assertiveness (respectful) | Calm, honest expression under pressure — a habit | L2 |

> **Why this shape:** communication is mostly **doing** (Skills), but it only *transfers* when paired
> with the **Abilities** that drive it — empathy (to adapt to the other person) and assertiveness (to
> say the hard thing kindly). Hence the Abilities are assessed **behaviorally, across ≥3 occasions**,
> not with a quiz.

## 📘 Learning objectives (Bloom + KSA)

| Objective | Bloom | KSA | Component | Target |
| --------- | ----- | --- | --------- | ------ |
| Explain the communication model and name common barriers (noise) | Understand | 🧠 K | K-comm-model | L2 |
| Analyze an audience and choose an appropriate channel | Understand/Analyze | 🧠 K | K-audience-channel | L2 |
| Listen actively: paraphrase, ask clarifying questions, check understanding | Apply | 🛠️ S | S-active-listening | L2 |
| Structure a clear message with BLUF/SBI/Pyramid (written & spoken) | Apply | 🛠️ S | S-structure-message | L2 |
| Give and receive feedback and de-escalate a difficult conversation | Apply | 🛠️ S | S-feedback-difficult | L2 |
| Adapt to the listener with empathy across multiple situations | Value (affective) | 🌱 A | A-empathy | L2 |
| Express needs assertively and respectfully under pressure | Respond (affective) | 🌱 A | A-assertiveness | L2 |

---

## 🔍 Phase planner

| Phase | Atom(s) | KSA focus | Activity | Assessment |
| ----- | ------- | --------- | -------- | ---------- |
| 🙉 1 · hear | Atom 1, 2 | 🧠 K | reading + video + the comm model; audience/channel worksheet | knowledge-mini (pop quizzes) |
| 🙈 2 · see | Atom 3 | 🛠️ S + 🌱 A | model active listening; paired listening practice | skill mini-rubric |
| 🙊 3 · do | Atom 4, 5 | 🛠️ S + 🌱 A | structure messages; feedback & difficult-conversation role-plays | performance task + behavioral assessment |
| 🐵 4 · share | Atom 6 (capstone) | 🛠️ S + 🌱 A | deliver a message + lead a conversation; showcase + peer review | capstone-5 |

---

## 🚀 Capstone & 📊 assessment

Full brief in [`capstone.md`](capstone.md); all rubrics in [`rubrics.md`](rubrics.md). In short:
formative pop quizzes for the Knowledge atoms, a skill mini-rubric + performance task for listening
and message structure, a **behavioral assessment** across occasions for the Abilities, and a live
communication performance graded on the standard 5-criteria capstone rubric. The badge → skills-map
mapping is in [`skills-map.md`](skills-map.md).

## 🎓 Outcomes & recognition

- A working model of how communication succeeds and fails (no more "they just didn't get it").
- Two job-ready moves: **active listening** and **structuring a clear message** (written & spoken).
- A repeatable approach to **feedback and difficult conversations**.
- The durable **empathy** and **assertiveness** that make communication land — evidenced over time.
- A portfolio artifact: a recorded/observed communication performance + reflection.
- LinkedIn-compatible digital badge: **🏅 Effective Communicator** — a multiplier on almost any role.
