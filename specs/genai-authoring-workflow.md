# 🤖 Gen AI Authoring Workflow

How to use a Gen AI assistant (Claude, GPT, Gemini, etc.) to go from a **job opportunity**
to a **designed ADA v2 micro-credential** and a learner **skills map** — fast, consistently,
and with **humans validating** the critical steps.

This is a **pipeline of prompts with fixed output schemas**. Each stage's output feeds the
next; each gated stage requires human sign-off before proceeding.

Prereqs: [`ksa-taxonomy.md`](ksa-taxonomy.md) ·
[`skills-map-and-job-matching.md`](skills-map-and-job-matching.md) ·
[`micro-credential-v2-schema.md`](micro-credential-v2-schema.md).

---

## Pipeline overview

```
 Stage 0  System grounding (load the ADA v2 specs)
 Stage 1  Extract Target KSA Profile      from a job posting        ▶ 🔒 HUMAN GATE
 Stage 2  Build the Skills Map            target − learner profile  ▶ 🔒 HUMAN GATE
 Stage 3  Design micro-credential(s)      one per gap cluster
 Stage 4  Design learning atoms           teach/assess to KSA type
 Stage 5  Generate typed rubrics & capstone
 Stage 6  Localize (ES / PT-BR)           keep parallel structure
 Stage 7  QA against conformance checklist                          ▶ 🔒 HUMAN GATE (badge)
```

> 🔒 **Human gates** (Stages 1, 2, 7): a mentor/employer must validate the target profile,
> the gap map, and any badge issuance. AI output is a **draft proposal** until signed off.

---

## Stage 0 — System grounding

Give the assistant the methodology as context. Suggested system prompt:

```
You are an ADA v2 curriculum-design assistant for Ada School.
Follow the ADA Methodology v2: learning atoms (Read·Listen·Watch·Practice·Evaluate·
Collaborate), 4 phases (hear→see→do→share), Bloom alignment, and the KSA framework
(Knowledge=know-what/why, Skill=know-how, Ability=durable/attitude).
Rules:
- Type every objective/atom as K, S, or A and assign a target level 0–4.
- Anchor competencies to SFIA/O*NET/ESCO/ILO when possible.
- Ensure each micro-credential covers ≥1 Skill and ≥1 Ability, not Knowledge only.
- Teach/assess each atom to its type (knowledge→quiz; skill→performance rubric;
  ability→behavioral rubric across ≥3 occasions + reflection).
- Output valid YAML/JSON matching the provided schemas. Flag every inference as
  "NEEDS HUMAN VALIDATION" where you are uncertain or where employer confirmation is required.
- Never assert a competency mapping or proficiency as final; you propose, humans validate.
```

---

## Stage 1 — Extract the Target KSA Profile  🔒

**Input:** a job posting (paste text) or a framework role (SFIA/O\*NET/ESCO id).

**Prompt template:**

```
From the job posting below, extract a Target KSA Profile.
For each requirement: classify as knowledge|skill|ability, give a stable id (prefix
K-/S-/A-), a label, a minimum proficiency level (0–4 per the ADA scale), a weight (1–5
importance), and must_have (true/false). Add Abilities the role implies even if not
stated explicitly, and mark those "inferred: true". Cite a framework_ref where possible.
Output YAML per the Target KSA Profile schema. List open questions for the employer.

JOB POSTING:
"""
<paste>
"""
```

**Output:** a `Target KSA Profile` (see schema in
[`skills-map-and-job-matching.md` §1.2](skills-map-and-job-matching.md)).

**🔒 Gate:** mentor/employer reviews — corrects levels/weights, confirms inferred Abilities,
removes hallucinated requirements. Postings under-state durable competencies; the human
adds the real Abilities.

---

## Stage 2 — Build the Skills Map  🔒

**Input:** validated Target KSA Profile + the learner's current profile (self-assessment +
imported badges).

**Prompt template:**

```
Given the validated Target KSA Profile and the Learner KSA Profile below, produce:
1) a Skills Map table (component, type, need, have, gap, status, must_have),
2) the job-match score and job_ready boolean (threshold 85%, blockers must be met),
3) an ordered "to_earn" plan (respect prerequisites, then weight),
4) a coverage-by-type check (warn if 0 abilities).
Output the minimal JSON object from the skills-map spec, plus the table in Markdown.

TARGET PROFILE: <yaml>
LEARNER PROFILE: <yaml>
```

**Output:** Skills Map table + match JSON (see §2–§6 of the skills-map spec).

**🔒 Gate:** mentor validates the learner's claimed current levels against evidence before
the plan is trusted.

---

## Stage 3 — Design the micro-credential(s)

**Input:** the `to_earn` list. Cluster related gaps into one or more micro-credentials
(10–30h, 4–8 atoms each).

**Prompt template:**

```
Design an ADA v2 micro-credential that closes these KSA gaps: <subset of to_earn>.
Produce the YAML front matter (micro-credential-v2-schema) + Markdown body:
title, duration, target role link, prerequisites, Bloom-aligned objectives each tagged
with its KSA component id and target level, the atom list, phase planner, capstone, and
typed assessment plan. Ensure ≥1 Skill and ≥1 Ability are covered.
```

**Output:** a v2 micro-credential file (front matter + body).

---

## Stage 4 — Design the learning atoms (to type)

For each KSA component, generate an atom **using the type-specific recipe**:

| If component is… | Tell the AI to emphasize… | Evaluate with… |
| ---------------- | ------------------------- | -------------- |
| 🧠 Knowledge | Read/Listen/Watch + retrieval practice | quiz / AI Q&A (accuracy) |
| 🛠️ Skill | short primer → hands-on lab/codelab with reps | performance rubric on artifact |
| 🌱 Ability | modeling + role-play/real collaboration across contexts + reflection | behavioral rubric across ≥3 occasions + journal |

**Prompt template:**

```
Design a learning atom for KSA component <id> (type: <k/s/a>, target level <n>).
Use the ADA learning-atom structure. Apply the <type> recipe: for ability, span multiple
occasions and require reflection; for skill, produce a concrete artifact; for knowledge,
include a concept check. Provide the matching rubric. Output per learning-atom-template.
```

---

## Stage 5 — Rubrics & capstone

```
Generate: (a) a mini-rubric for each atom matched to its KSA type, and (b) a capstone that
integrates the micro-credential's K + S + A in one realistic job task, scored with the
5-criteria ADA capstone rubric, with a row showing which KSA each criterion evidences.
```

---

## Stage 6 — Localize

```
Translate the micro-credential into Spanish (templates/es) and Portuguese-BR
(templates/pt-br). Keep section structure parallel to the English source. Do not alter the
KSA ids or levels (they are language-neutral).
```

---

## Stage 7 — QA & badge issuance  🔒

Run the **conformance checklist** from
[`ada-v2-ksa-framework.md` §10](ada-v2-ksa-framework.md) automatically:

```
Audit this micro-credential against the ADA v2 conformance checklist. For each item return
pass/fail + fix. Confirm every objective has a KSA type + level, ≥1 skill and ≥1 ability
are present, abilities are assessed across ≥3 occasions, and machine-readable tags are valid.
```

**🔒 Gate:** a human signs off the QA report; **badges are issued only on verified evidence**,
never on AI judgement alone.

---

## Anti-hallucination & quality rules

- **Cite or flag:** every framework_ref and external resource is either a real link or
  marked `NEEDS HUMAN VALIDATION`.
- **No invented levels:** the AI proposes proficiency; the human confirms against evidence.
- **Schema-locked output:** reject free-form output; require the YAML/JSON schemas so the
  result is machine-consumable by the skills-map tooling.
- **Bias check on Abilities:** prompt the AI to surface durable/attitudinal competencies
  postings omit, then have the employer confirm them.
- **Keep it accessible:** prefer free tools and openly licensed resources.
- **Log the loop:** store prompts + human edits for auditability and reuse.

---

## End-to-end example

A complete run of this pipeline (posting → profile → map → micro-credentials → match) is
in [`../examples/skills-map-job-match-frontend.md`](../examples/skills-map-job-match-frontend.md).
