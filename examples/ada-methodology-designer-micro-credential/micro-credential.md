# 🎓 Micro-Credential — ADA Methodology Designer

The full specification for this micro-credential. It conforms to
[`../../specs/micro-credential-v2-schema.md`](../../specs/micro-credential-v2-schema.md).

---

## YAML front matter

```yaml
schema: ada-microcredential/v2
id: mc-ada-methodology-designer
title: "ADA Methodology Designer"
language: en
duration_hours: 20
level: intermediate
status: published
license: CC-BY-SA-4.0
mentors: ["@sancarbar"]

target_roles:
  - role: "Instructional designer / curriculum author / L&D lead / mentor authoring ADA credentials"
    framework_ref: >
      O*NET 25-9031.00 Instructional Coordinators ·
      ESCO "develop curriculum", "design pedagogical approaches", "create learning materials" ·
      SFIA: LEDA (learning & development), KNOW (knowledge management)

ksa:
  - { id: K-ada-architecture, type: knowledge, label: "ADA building blocks & flow (skill need → micro-credential → phases → atoms → capstone → badge → skills map)", target_level: 2, bloom: understand }
  - { id: K-ksa-framework,    type: knowledge, label: "KSA types, the 0-4 proficiency scale, the affective domain, and how to classify a competency", target_level: 3, bloom: analyze }
  - { id: K-bloom,            type: knowledge, label: "Bloom's revised cognitive + affective taxonomies; writing measurable objectives", target_level: 2, bloom: understand }
  - { id: K-topology,         type: knowledge, label: "The 7 modalities and their sub-types; modality↔KSA and modality↔phase fit", target_level: 2, bloom: understand }
  - { id: S-write-objectives, type: skill,     label: "Write Bloom-verb objectives tagged with KSA type + target level", target_level: 2, bloom: apply }
  - { id: S-design-atoms,     type: skill,     label: "Design learning atoms of each KSA type with topology-correct modalities", target_level: 3, bloom: create, primary: true }
  - { id: S-build-rubric,     type: skill,     label: "Build the 5-criteria Assessment Rubric + mini-rubrics; map evidence → badge", target_level: 2, bloom: apply }
  - { id: S-assemble-mc,      type: skill,     label: "Assemble a complete micro-credential from the ADA templates", target_level: 3, bloom: create, primary: true }
  - { id: A-design-judgment,  type: ability,   label: "Design with learner empathy, framework rigor, and human-in-the-loop judgment", target_level: 2, affective_stage: value, assessed_occasions: 3 }

atoms:
  - { id: atom-1, title: "The ADA big picture", ksa_refs: [K-ada-architecture], phase: 1, modalities: [{dimension: read, subtype: Article}, {dimension: see, subtype: Flowchart}, {dimension: evaluate, subtype: Pop Quiz}], rubric: knowledge-mini }
  - { id: atom-2, title: "KSA in depth", ksa_refs: [K-ksa-framework], phase: 1, modalities: [{dimension: read, subtype: Technical Article}, {dimension: see, subtype: Framework}, {dimension: practice, subtype: Worksheet / Exercise}, {dimension: evaluate, subtype: Mini-Rubric}], rubric: knowledge-mini }
  - { id: atom-3, title: "Bloom's taxonomy & measurable objectives", ksa_refs: [K-bloom, S-write-objectives], phase: 1, modalities: [{dimension: read, subtype: Technical Article}, {dimension: see, subtype: Diagram}, {dimension: practice, subtype: Worksheet / Exercise}, {dimension: evaluate, subtype: Mini-Rubric}], rubric: skill }
  - { id: atom-4, title: "The learning atom topology", ksa_refs: [K-topology], phase: 2, modalities: [{dimension: see, subtype: Mind Map}, {dimension: read, subtype: Documentation / Reference}, {dimension: practice, subtype: Design Exercise}, {dimension: evaluate, subtype: Pop Quiz}], rubric: knowledge-mini }
  - { id: atom-5, title: "Build one atom of each KSA type", ksa_refs: [S-design-atoms, A-design-judgment], phase: 3, modalities: [{dimension: practice, subtype: Design Exercise}, {dimension: collaborate, subtype: Async Peer Review}, {dimension: evaluate, subtype: Performance Task}], rubric: skill }
  - { id: atom-6, title: "Design the assessment", ksa_refs: [S-build-rubric], phase: 3, modalities: [{dimension: practice, subtype: Design Exercise}, {dimension: evaluate, subtype: Performance Task}], rubric: skill }
  - { id: atom-7, title: "Capstone — assemble the full credential", ksa_refs: [S-assemble-mc, A-design-judgment], phase: 4, modalities: [{dimension: practice, subtype: Project Task}, {dimension: collaborate, subtype: Showcase / Demo Day}, {dimension: evaluate, subtype: Capstone Project}], rubric: capstone-5 }

capstone:
  title: "Design a complete ADA micro-credential for a real organizational skill need"
  integrates_ksa: [K-ada-architecture, K-ksa-framework, K-bloom, K-topology, S-write-objectives, S-design-atoms, S-build-rubric, S-assemble-mc, A-design-judgment]
  rubric: capstone-5

badge:
  name: "ADA Methodology Designer"
  evidence_required: ["atom-5", "atom-6", "capstone"]
  issued_on: verified-evidence
```

---

## 🩺 Before you start — diagnostic (optional)

Rate yourself **0–4** (the ADA proficiency scale taught in Atom 2) on each component, then re-rate
at the end — the delta is your evidence of growth.

| Component | 0–4 now | 0–4 after |
| --------- | :-----: | :-------: |
| Explain the ADA architecture | ☐ | ☐ |
| Classify a competency as K/S/A | ☐ | ☐ |
| Write a Bloom-verb objective | ☐ | ☐ |
| Pick modalities for an atom | ☐ | ☐ |
| Build an assessment rubric | ☐ | ☐ |
| Assemble a full micro-credential | ☐ | ☐ |

---

## 🎯 Target job competency

Design and author **ADA micro-credentials** that turn a real role/skill need into a measurable,
job-matchable learning unit. Appears in postings as *"instructional design", "curriculum
development", "learning experience design", "create learning materials", "competency mapping".*
Mapped to **O\*NET 25-9031.00** (Instructional Coordinators), **ESCO** *"develop curriculum / design
pedagogical approaches"*, and **SFIA LEDA / KNOW**.

## 🧬 KSA breakdown — what mastery means here

| KSA | Component | Why this type | Target |
| --- | --------- | ------------- | ------ |
| 🧠 Knowledge | ADA architecture & flow | The map you reason from | L2 |
| 🧠 Knowledge | KSA framework + 0–4 scale + affective domain | The classification engine of v2 | **L3** |
| 🧠 Knowledge | Bloom's cognitive + affective taxonomies | How objectives become measurable | L2 |
| 🧠 Knowledge | The 7-modality topology | The menu you design atoms from | L2 |
| 🛠️ Skill | Write Bloom + KSA objectives | A repeatable authoring move | L2 |
| 🛠️ Skill | Design atoms of each KSA type | The core craft — practiced for real | **L3** |
| 🛠️ Skill | Build the Assessment Rubric | Makes learning measurable & fair | L2 |
| 🛠️ Skill | Assemble a full micro-credential | The end-to-end deliverable | **L3** |
| 🌱 Ability | Instructional-design judgment | Empathy + rigor + human-in-the-loop, shown across the build | L2 |

> **Why this shape:** designing curriculum is mostly **doing** (Skills at L3 — *Create*), resting on
> a solid **Knowledge** base (KSA, Bloom, topology) and a durable **Ability** — the judgment to keep
> the learner central, cite frameworks honestly, and flag what a human must validate.

## 📘 Learning objectives (Bloom + KSA)

| Objective | Bloom | KSA | Component | Target |
| --------- | ----- | --- | --------- | ------ |
| Explain how the ADA building blocks fit together | Understand | 🧠 K | K-ada-architecture | L2 |
| Classify any competency as K/S/A and set a 0–4 target | Analyze | 🧠 K | K-ksa-framework | L3 |
| Write measurable objectives using Bloom verbs, tagged with KSA | Apply | 🛠️ S | S-write-objectives | L2 |
| Select topology modalities that fit an atom's KSA type and phase | Understand/Apply | 🧠 K | K-topology | L2 |
| Design a Knowledge, a Skill, and an Ability atom | Create | 🛠️ S | S-design-atoms | L3 |
| Build a 5-criteria Assessment Rubric and an evidence→badge map | Apply | 🛠️ S | S-build-rubric | L2 |
| Assemble a complete, job-ready ADA micro-credential | Create | 🛠️ S | S-assemble-mc | L3 |
| Design with learner empathy and human-in-the-loop rigor | Value (affective) | 🌱 A | A-design-judgment | L2 |

---

## 🔍 Phase planner

| Phase | Atom(s) | KSA focus | Activity | Assessment |
| ----- | ------- | --------- | -------- | ---------- |
| 🙉 1 · hear | Atom 1, 2, 3 | 🧠 K → 🛠️ S | read + diagrams; classify competencies; write objectives | knowledge-mini + skill mini-rubric |
| 🙈 2 · see | Atom 4 | 🧠 K | study the topology mind map; choose modalities | pop quiz + design exercise |
| 🙊 3 · do | Atom 5, 6 | 🛠️ S + 🌱 A | author 3 atoms; build the rubric | performance tasks + peer review |
| 🐵 4 · share | Atom 7 (capstone) | 🛠️ S + 🌱 A | assemble the full credential; showcase + peer review | capstone-5 |

---

## 🚀 Capstone & 📊 assessment

Full brief in [`capstone.md`](capstone.md); all rubrics in [`rubrics.md`](rubrics.md). In short:
formative pop quizzes / mini-rubrics for the Knowledge atoms, a skill mini-rubric + performance task
for the design atoms, and a **complete ADA credential the learner designs**, graded on the standard
5-criteria capstone rubric. The badge → skills-map mapping is in [`skills-map.md`](skills-map.md).

## 🎓 Outcomes & recognition

- Fluency in the ADA building blocks, the KSA framework, Bloom, and the learning-atom topology.
- The craft of authoring atoms of every KSA type and building assessment rubrics.
- A portfolio artifact: a complete, job-ready **ADA micro-credential the learner designed** end to end.
- LinkedIn-compatible digital badge: **🏅 ADA Methodology Designer** — the entry point to an
  instructional-design / L&D pathway.
