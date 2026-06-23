# 🎓 Micro-Credential — Problem Solving: Define, Diagnose & Decide

The full specification for this micro-credential. It conforms to
[`../../specs/micro-credential-v2-schema.md`](../../specs/micro-credential-v2-schema.md).

---

## YAML front matter

```yaml
schema: ada-microcredential/v2
id: mc-problem-solving
title: "Problem Solving: Define, Diagnose & Decide"
language: en
duration_hours: 12
level: beginner
status: published
license: CC-BY-SA-4.0
mentors: ["@sancarbar"]

target_roles:
  - role: "Any role — problem solving is a transversal, near-universal job requirement (ICs, leads, analysts, operators, founders)"
    framework_ref: >
      O*NET: 2.B.2.i Complex Problem Solving, 2.A.2.a Critical Thinking, 2.B.4.e Judgment and Decision Making ·
      ESCO transversal: "solve problems", "think analytically", "think critically"

ksa:
  - { id: K-process,          type: knowledge, label: "The problem-solving process (define→diagnose→generate→decide→implement→review) and mindset (symptom vs root cause; divergent vs convergent)", target_level: 2, bloom: understand }
  - { id: K-decisions-biases, type: knowledge, label: "Decision-making basics (criteria, trade-offs) and common cognitive biases that derail problem solving", target_level: 2, bloom: understand }
  - { id: S-frame,            type: skill,     label: "Define and decompose a problem: write a clear problem statement, break it down, use first principles", target_level: 2, bloom: apply, primary: true }
  - { id: S-root-cause,       type: skill,     label: "Find the root cause: 5 Whys, fishbone (Ishikawa), and simple hypothesis testing", target_level: 2, bloom: apply, primary: true }
  - { id: S-solutions,        type: skill,     label: "Generate options (divergent) and choose well (convergent) using a decision matrix and trade-offs", target_level: 2, bloom: apply }
  - { id: A-persistence,      type: ability,   label: "Persistence and tolerance for ambiguity: stay with a hard, unclear problem without forcing a premature answer", target_level: 2, affective_stage: respond, assessed_occasions: 3 }
  - { id: A-critical-curious, type: ability,   label: "Critical, curious thinking: question assumptions and ask 'why/what if' rather than accept the obvious", target_level: 2, affective_stage: value, assessed_occasions: 3 }

atoms:
  - { id: atom-1, title: "How problem solving works", ksa_refs: [K-process], phase: 1, modalities: [{dimension: read, subtype: Article}, {dimension: watch, subtype: Video Explainer}, {dimension: see, subtype: Mental Model}, {dimension: evaluate, subtype: Pop Quiz}], rubric: knowledge-mini }
  - { id: atom-2, title: "Decisions & cognitive biases", ksa_refs: [K-decisions-biases], phase: 1, modalities: [{dimension: read, subtype: Article}, {dimension: watch, subtype: Video Explainer}, {dimension: see, subtype: Framework}, {dimension: evaluate, subtype: Pop Quiz}], rubric: knowledge-mini }
  - { id: atom-3, title: "Define & decompose the problem", ksa_refs: [S-frame], phase: 2, modalities: [{dimension: see, subtype: Diagram}, {dimension: practice, subtype: Worksheet / Exercise}, {dimension: practice, subtype: AI Prompt Question}, {dimension: evaluate, subtype: Performance Task}], rubric: skill }
  - { id: atom-4, title: "Find the root cause", ksa_refs: [S-root-cause], phase: 3, modalities: [{dimension: read, subtype: Technical Article}, {dimension: practice, subtype: Case Study}, {dimension: practice, subtype: Worksheet / Exercise}, {dimension: evaluate, subtype: Performance Task}], rubric: skill }
  - { id: atom-5, title: "Generate & choose solutions", ksa_refs: [S-solutions, A-persistence, A-critical-curious], phase: 3, modalities: [{dimension: practice, subtype: Challenge / Quest}, {dimension: practice, subtype: Simulation}, {dimension: collaborate, subtype: Pair Programming}, {dimension: evaluate, subtype: Behavioral Assessment}], rubric: behavioral }
  - { id: atom-6, title: "Capstone: solve a real problem end-to-end", ksa_refs: [S-frame, S-root-cause, S-solutions, A-persistence, A-critical-curious], phase: 4, modalities: [{dimension: practice, subtype: Project / Quest}, {dimension: collaborate, subtype: Showcase / Demo Day}, {dimension: collaborate, subtype: Async Peer Review}, {dimension: evaluate, subtype: Capstone Project}], rubric: capstone-5 }

capstone:
  title: "Take a real, messy problem from definition to a defended, decided solution — and document the process"
  integrates_ksa: [K-process, K-decisions-biases, S-frame, S-root-cause, S-solutions, A-persistence, A-critical-curious]
  rubric: capstone-5

badge:
  name: "Problem Solver"
  evidence_required: ["atom-3", "atom-4", "atom-5", "capstone"]
  issued_on: verified-evidence
```

---

## 🎯 Target job competency

**Solve problems methodically.** Employers don't just want answers — they want people who can take an
ambiguous, messy situation, **figure out what the real problem is**, **diagnose why it's happening**,
and **choose a defensible solution** under constraints. It is one of the most-requested competencies
across every function. Mapped to **O\*NET** (Complex Problem Solving, Critical Thinking, Judgment &
Decision Making) and **ESCO** transversal *"solve problems / think analytically."*

## 🧬 KSA breakdown — a cognitive skill, taught the right way

| KSA | Component | Why this type | Target |
| --- | --------- | ------------- | ------ |
| 🧠 Knowledge | The problem-solving process & mindset | A mental model that stops "solution-jumping" | L2 |
| 🧠 Knowledge | Decisions & cognitive biases | You can't counter biases you can't name | L2 |
| 🛠️ Skill | Define & decompose | A trainable technique (problem statement, breakdown) | **L2** |
| 🛠️ Skill | Root cause analysis | 5 Whys / fishbone / hypotheses — practiced on cases | **L2** |
| 🛠️ Skill | Generate & choose solutions | Divergent options + convergent decision matrix | L2 |
| 🌱 Ability | Persistence & ambiguity tolerance | A disposition shown across situations, over time | L2 |
| 🌱 Ability | Critical, curious thinking | A habit of questioning assumptions | L2 |

> **Why this shape:** problem solving is mostly **doing** (Skills: frame, diagnose, decide), but it
> only *works* when paired with the **Abilities** that drive it — persistence (to stay with hard,
> unclear problems) and critical curiosity (to question the obvious). Those Abilities are assessed
> **behaviorally, across ≥3 occasions**, not with a quiz.

## 📘 Learning objectives (Bloom + KSA)

| Objective | Bloom | KSA | Component | Target |
| --------- | ----- | --- | --------- | ------ |
| Explain the problem-solving process and distinguish symptom from root cause | Understand | 🧠 K | K-process | L2 |
| Recognize common cognitive biases and how they distort decisions | Understand | 🧠 K | K-decisions-biases | L2 |
| Write a clear problem statement and decompose a problem | Apply | 🛠️ S | S-frame | L2 |
| Find a root cause using 5 Whys / fishbone / hypothesis testing | Apply | 🛠️ S | S-root-cause | L2 |
| Generate options and choose one with a decision matrix and trade-offs | Apply | 🛠️ S | S-solutions | L2 |
| Persist with ambiguous problems without forcing a premature answer | Respond (affective) | 🌱 A | A-persistence | L2 |
| Question assumptions and pursue "why/what if" across situations | Value (affective) | 🌱 A | A-critical-curious | L2 |

---

## 🔍 Phase planner

| Phase | Atom(s) | KSA focus | Activity | Assessment |
| ----- | ------- | --------- | -------- | ---------- |
| 🙉 1 · hear | Atom 1, 2 | 🧠 K | reading + video on the process; biases framework | knowledge-mini (pop quizzes) |
| 🙈 2 · see | Atom 3 | 🛠️ S | model problem framing; write & decompose a real problem statement | performance task |
| 🙊 3 · do | Atom 4, 5 | 🛠️ S + 🌱 A | root-cause a case; generate & choose under trade-offs | performance task + behavioral assessment |
| 🐵 4 · share | Atom 6 (capstone) | 🛠️ S + 🌱 A | solve a real problem end-to-end; defend + peer review | capstone-5 |

---

## 🚀 Capstone & 📊 assessment

Full brief in [`capstone.md`](capstone.md); all rubrics in [`rubrics.md`](rubrics.md). In short:
formative pop quizzes for the Knowledge atoms, skill performance tasks for framing and root-cause,
a **behavioral assessment** across occasions for the Abilities, and a real end-to-end problem solved,
documented, and defended on the standard 5-criteria capstone rubric. The badge → skills-map mapping
is in [`skills-map.md`](skills-map.md).

## 🎓 Outcomes & recognition

- A repeatable process that replaces "solution-jumping" with **define → diagnose → decide**.
- The ability to write a sharp **problem statement** and **decompose** complexity.
- Working **root-cause analysis** (5 Whys, fishbone, hypotheses).
- A defensible way to **generate options and choose** under trade-offs (decision matrix).
- The durable **persistence** and **critical curiosity** that make it stick — evidenced over time.
- A portfolio artifact: a real problem solved end-to-end with the reasoning documented.
- LinkedIn-compatible digital badge: **🏅 Problem Solver** — a multiplier on almost any role.
