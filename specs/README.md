# 🧬 ADA v2 Specifications — KSA-Driven, Job-Matched, Gen AI-Authored

<p align="center">
  <img alt="Indigo #1E2A6E" src="https://img.shields.io/badge/Indigo-1E2A6E?style=flat-square&labelColor=1E2A6E&color=1E2A6E">
  <img alt="Turquoise #15B5C6" src="https://img.shields.io/badge/Turquoise-15B5C6?style=flat-square&labelColor=15B5C6&color=15B5C6">
  <img alt="Gold #E0A53C" src="https://img.shields.io/badge/Gold-E0A53C?style=flat-square&labelColor=E0A53C&color=E0A53C">
  <img alt="Ink #0A1124" src="https://img.shields.io/badge/Ink-0A1124?style=flat-square&labelColor=0A1124&color=0A1124">
</p>

This folder specifies **ADA Methodology v2**: an evolution of the ADA (Applied Digital
Apprenticeship) framework that makes the methodology **competency-precise** and
**job-matchable** by adopting the **KSA framework — Knowledge, Skills, Abilities** — and a
**Gen AI authoring workflow** that turns a real job opportunity into a designed
micro-credential and a personalized **skills map**.

> v2 **layers onto** v1 — it does not replace it. Learning Atoms, the 4 Phases, Bloom
> alignment, capstones, and rubrics all remain. v2 adds a competency spine (KSA), a
> matchable graph (skills map), and a repeatable Gen AI design loop.

<p align="center">
  <img alt="The ADA Methodology overview: philosophy, 4 phases, and learning atoms forming micro-credentials" src="../img/ada-methodology-overview.png" width="900">
</p>

---

## Why v2

ADA v1 reliably produces well-structured learning. But it leaves three questions
under-specified:

1. **What *kind* of competency is each objective developing?** A coding lab, a feedback
   conversation, and a display of perseverance are not the same thing, and shouldn't be
   taught or assessed the same way. → **KSA framework.**
2. **How does a learner know they're ready for a specific job?** v1 aligns to frameworks
   but doesn't model the *gap* between a person and a role. → **Skills map + job matching.**
3. **How do we design all this fast, consistently, and at scale?** → **Gen AI authoring
   workflow** with fixed schemas and a human-in-the-loop.

---

## The v2 model in one picture

```
        ┌──────────────────────────────────────────────────────────────┐
        │  JOB OPPORTUNITY (posting / role / framework: SFIA·O*NET·ESCO) │
        └───────────────────────────────┬──────────────────────────────┘
                                         │  Gen AI extraction
                                         ▼
        ┌──────────────────────────────────────────────────────────────┐
        │  TARGET KSA PROFILE  →  required Knowledge · Skills · Abilities │
        │                         each with a minimum proficiency level   │
        └───────────────────────────────┬──────────────────────────────┘
                                         │  diff vs. learner's current profile
                                         ▼
        ┌──────────────────────────────────────────────────────────────┐
        │  SKILLS MAP (gap graph): the KSA you must EARN to qualify       │
        └───────────────────────────────┬──────────────────────────────┘
                                         │  Gen AI design (per KSA node)
                                         ▼
        ┌──────────────────────────────────────────────────────────────┐
        │  MICRO-CREDENTIALS → LEARNING ATOMS (Read·Listen·Watch·        │
        │  Practice·Evaluate·Collaborate) across the 4 ADA Phases        │
        └───────────────────────────────┬──────────────────────────────┘
                                         │  evidence + rubric assessment
                                         ▼
        ┌──────────────────────────────────────────────────────────────┐
        │  VERIFIED BADGES → updated skills map → JOB-READY MATCH %       │
        └──────────────────────────────────────────────────────────────┘
                              ▲ human-in-the-loop validation at each stage ▲
```

---

## What's in this folder

| Spec | Purpose |
| ---- | ------- |
| [`ada-v2-ksa-framework.md`](ada-v2-ksa-framework.md) | The core v2 specification. How KSA integrates with atoms, phases, Bloom, and the full design lifecycle. **Start here.** |
| [`role-to-credential-mapping.md`](role-to-credential-mapping.md) | The methodology for **deconstructing a real job/role into a pathway of micro-credentials** — triangulating frameworks, live demand, and **observation of high performers** (DACUM · BEI · shadowing) into measurable KSA, with AI prompts and human gates. |
| [`learning-atom-topology.md`](learning-atom-topology.md) | The complete, diagrammed topology of Learning Atom modalities and sub-types (Read · Listen · Watch · See · Practice · Evaluate · Collaborate) with selection guidance and KSA/Phase mappings. |
| [`ksa-taxonomy.md`](ksa-taxonomy.md) | Precise definitions of Knowledge, Skills, Abilities; how to classify any competency; proficiency scales; assessment fit; mapping to Bloom, atom formats, and frameworks. |
| [`skills-map-and-job-matching.md`](skills-map-and-job-matching.md) | Data model for a target KSA profile, a learner profile, the gap-based **skills map**, and the **job-match score**. |
| [`genai-authoring-workflow.md`](genai-authoring-workflow.md) | The repeatable Gen AI pipeline (prompts + JSON schemas) that goes from a job posting to a designed micro-credential, with human review gates. |
| [`micro-credential-v2-schema.md`](micro-credential-v2-schema.md) | The KSA-aware, machine-readable schema/template for a v2 micro-credential (YAML front matter + Markdown body). |

## Worked examples (in [`../examples/`](../examples/))

These demonstrate v2 across the three KSA "flavors":

- **Technical Skill** → [`ksa-technical-skill-rest-api.md`](../examples/ksa-technical-skill-rest-api.md)
- **Human / durable Skill** → [`ksa-human-skill-feedback.md`](../examples/ksa-human-skill-feedback.md)
- **Attitude / Ability** → [`ksa-attitude-adaptability.md`](../examples/ksa-attitude-adaptability.md)
- **End-to-end job match** → [`skills-map-job-match-frontend.md`](../examples/skills-map-job-match-frontend.md)
- **Role → pathway (job deconstruction)** → [`role-data-scientist-pathway.md`](../examples/role-data-scientist-pathway.md)

---

## Design principles for v2

1. **Every objective is typed (K / S / A).** No untyped learning.
2. **Teach and assess to the type.** Knowledge ≠ Skill ≠ Ability in method or evidence.
3. **Everything is matchable.** Competencies carry a proficiency level so gaps are computable.
4. **Gen AI drafts; humans validate.** Mentors/employers confirm mappings and proficiency.
5. **Evidence over completion.** A badge means demonstrated KSA, not time served.
6. **Backward compatible.** A v1 micro-credential is a valid v2 one with KSA tags added.

---

> License: CC BY-SA 4.0 · Maintained by [Ada School](https://ada-school.org/).
