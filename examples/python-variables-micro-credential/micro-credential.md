# 🎓 Micro-Credential — Python Variables: Store, Name & Use Data

The full specification for this micro-credential. It conforms to
[`../../specs/micro-credential-v2-schema.md`](../../specs/micro-credential-v2-schema.md).

---

## YAML front matter

```yaml
schema: ada-microcredential/v2
id: mc-python-variables-basics
title: "Python Variables: Store, Name & Use Data"
language: en
duration_hours: 6
level: beginner
status: published
license: CC-BY-SA-4.0
mentors: ["@sancarbar"]

target_roles:
  - role: "Entry-level Software Developer / Programmer / Data Analyst (first Python skill)"
    framework_ref: >
      SFIA: PROG (programming/software development) level 1-2 ·
      O*NET 15-1251.00 Computer Programmers, 15-1252.00 Software Developers ·
      ESCO: "use a programming language", "Python (computer programming)"

ksa:
  - { id: K-var-concept,   type: knowledge, label: "What a variable is: a name bound to a value; the label/box mental model; dynamic typing", target_level: 1, bloom: understand }
  - { id: K-data-types,    type: knowledge, label: "Core built-in types (int, float, str, bool), type(), and how/why values convert", target_level: 2, bloom: understand }
  - { id: S-declare-assign, type: skill,    label: "Declare, assign, and reassign variables with valid, readable PEP 8 names", target_level: 2, bloom: apply, primary: true }
  - { id: S-use-values,    type: skill,     label: "Use variables in expressions, convert types, and format output with f-strings", target_level: 2, bloom: apply, primary: true }
  - { id: A-attention-detail, type: ability, label: "Read errors and fix naming/type bugs; write clean, readable code (a debugging mindset)", target_level: 2, affective_stage: value, assessed_occasions: 3 }

atoms:
  - { id: atom-1, title: "What is a variable?", ksa_refs: [K-var-concept], phase: 1, modalities: [{dimension: read, subtype: Article}, {dimension: watch, subtype: Video Explainer}, {dimension: see, subtype: Mental Model}, {dimension: evaluate, subtype: Pop Quiz}], rubric: knowledge-mini }
  - { id: atom-2, title: "Data types & dynamic typing", ksa_refs: [K-data-types, K-var-concept], phase: 2, modalities: [{dimension: read, subtype: Article}, {dimension: see, subtype: Diagram}, {dimension: watch, subtype: Short}, {dimension: evaluate, subtype: Pop Quiz}], rubric: knowledge-mini }
  - { id: atom-3, title: "Naming & assignment codelab", ksa_refs: [S-declare-assign, A-attention-detail], phase: 3, modalities: [{dimension: read, subtype: Technical Article}, {dimension: practice, subtype: Codelab}, {dimension: evaluate, subtype: Mini-Rubric}], rubric: skill }
  - { id: atom-4, title: "Expressions, conversion & f-strings codelab", ksa_refs: [S-use-values, A-attention-detail], phase: 3, modalities: [{dimension: watch, subtype: Tutorial / Screencast}, {dimension: practice, subtype: Codelab}, {dimension: practice, subtype: AI Prompt Question}, {dimension: evaluate, subtype: Performance Task}], rubric: skill }
  - { id: atom-5, title: "Mini-project (capstone) + peer review", ksa_refs: [S-declare-assign, S-use-values, A-attention-detail], phase: 4, modalities: [{dimension: practice, subtype: Project Task}, {dimension: collaborate, subtype: Pair Programming}, {dimension: collaborate, subtype: Showcase / Demo Day}, {dimension: evaluate, subtype: Performance Task}], rubric: capstone-5 }

capstone:
  title: "Build a small program that stores, converts, and prints data with variables"
  integrates_ksa: [K-var-concept, K-data-types, S-declare-assign, S-use-values, A-attention-detail]
  rubric: capstone-5

badge:
  name: "Python Variables Foundations"
  evidence_required: ["atom-3", "atom-4", "capstone"]
  issued_on: verified-evidence
```

---

## 🎯 Target job competency

Write basic Python that **stores and manipulates data using variables** — the foundation of every
script, notebook, and app. Appears in postings as *"Python (basic)", "scripting", "able to write
simple programs", "data manipulation".* Mapped to **SFIA PROG** (level 1–2), **O\*NET** Programmer /
Software Developer tasks, and **ESCO** *"use a programming language / Python"*.

## 🧬 KSA breakdown — a first skill, taught the right way

| KSA | Component | Why this type | Target |
| --- | --------- | ------------- | ------ |
| 🧠 Knowledge | What a variable is (name → value; the label model; dynamic typing) | A small mental model you must *understand* before coding | L1 |
| 🧠 Knowledge | Core data types & conversion (`int`, `float`, `str`, `bool`) | Prevents the #1 beginner bug ("number is a string") | L2 |
| 🛠️ Skill | Declare / name / reassign variables (PEP 8) | A concrete move practiced in a codelab | **L2** |
| 🛠️ Skill | Use variables in expressions, convert types, f-strings | The *useful* payoff — make the data do something | **L2** |
| 🌱 Ability | Attention to detail / debugging mindset | Reading errors & fixing typos is a habit, shown across reps | L2 |

> **Why this shape:** a coding skill is mostly **doing**, with just enough **Knowledge** to avoid
> classic traps, plus the budding **Ability** to slow down, read an error, and fix it — the habit
> that separates someone who "did a tutorial" from someone who can actually program.

## 📘 Learning objectives (Bloom + KSA)

| Objective | Bloom | KSA | Component | Target |
| --------- | ----- | --- | --------- | ------ |
| Explain what a variable is and how a name is bound to a value | Understand | 🧠 K | K-var-concept | L1 |
| Identify Python's core data types and predict `type()` results | Understand | 🧠 K | K-data-types | L2 |
| Declare, assign, and reassign variables with readable PEP 8 names | Apply | 🛠️ S | S-declare-assign | L2 |
| Use variables in expressions, convert types, and format with f-strings | Apply | 🛠️ S | S-use-values | L2 |
| Organize logic into functions with a `main()` runner | Apply | 🛠️ S | S-use-values | L2 |
| Write and run a basic unit test (`unittest`) to verify a function | Apply | 🌱 A | A-attention-detail | L2 |
| Read an error message and fix a naming/type bug | Apply | 🌱 A | A-attention-detail | L2 |

---

## 🔍 Phase planner

| Phase | Atom(s) | KSA focus | Activity | Assessment |
| ----- | ------- | --------- | -------- | ---------- |
| 🙉 1 · hear | Atom 1 | 🧠 K | reading + video + the "label" mental model | knowledge-mini (pop quiz) |
| 🙈 2 · see | Atom 2 | 🧠 K | data-types diagram + short + `type()` exploration | knowledge-mini (pop quiz) |
| 🙊 3 · do | Atom 3, Atom 4 | 🛠️ S + 🌱 A | naming/assignment codelab; expressions, conversion & f-strings | skill mini-rubric + performance task |
| 🐵 4 · share | Atom 5 (capstone) | 🛠️ S + 🌱 A | ship a small program; pair + showcase + peer review | capstone-5 |

---

## 🚀 Capstone & 📊 assessment

Full brief in [`capstone.md`](capstone.md); all rubrics in [`rubrics.md`](rubrics.md). In short:
formative pop quizzes for the Knowledge atoms, a skill mini-rubric + performance task for the
codelabs, and a small shippable program graded on the standard 5-criteria capstone rubric. The
badge → skills-map mapping is in [`skills-map.md`](skills-map.md).

## 🎓 Outcomes & recognition

- An accurate mental model of variables, types, and dynamic typing (no magic).
- Two job-ready moves: declaring/naming variables well, and using/converting/formatting values.
- The habit of structuring code into functions with a `main()` and **verifying it with unit tests**.
- A portfolio artifact: a small, working, **tested** Python program you wrote and explained.
- LinkedIn-compatible digital badge: **🏅 Python Variables Foundations** — the first step on a
  developer or data pathway.
