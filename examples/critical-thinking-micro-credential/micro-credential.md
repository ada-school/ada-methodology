# 🎓 Micro-Credential — Critical Thinking: Reason, Evaluate & Judge

The full specification for this micro-credential. It conforms to
[`../../specs/micro-credential-v2-schema.md`](../../specs/micro-credential-v2-schema.md).

---

## YAML front matter

```yaml
schema: ada-microcredential/v2
id: mc-critical-thinking
title: "Critical Thinking: Reason, Evaluate & Judge"
language: en
duration_hours: 12
level: beginner
status: published
license: CC-BY-SA-4.0
mentors: ["@sancarbar"]

target_roles:
  - role: "Any role — critical thinking is a transversal, near-universal job requirement (analysts, ICs, leads, researchers, founders)"
    framework_ref: >
      O*NET process skills: 2.A.2.a Critical Thinking, 2.A.2.a Active Learning, 2.B.4.e Judgment and Decision Making ·
      ESCO transversal: "think critically", "think analytically", "process information"

ksa:
  - { id: K-reasoning,            type: knowledge, label: "The anatomy of reasoning: claims, premises, assumptions, inference; validity vs. soundness; standards of good thinking (clarity, accuracy, relevance, logic, fairness)", target_level: 2, bloom: understand }
  - { id: K-fallacies-biases,     type: knowledge, label: "Common logical fallacies and reasoning biases that make thinking fail", target_level: 2, bloom: understand }
  - { id: S-evaluate-arguments,   type: skill,     label: "Deconstruct and evaluate an argument and its evidence: identify claim/premises/assumptions, assess evidence quality and logical strength", target_level: 2, bloom: analyze, primary: true }
  - { id: S-question-verify,      type: skill,     label: "Ask good questions and verify: Socratic questioning, source/credibility evaluation, steelmanning", target_level: 2, bloom: apply, primary: true }
  - { id: S-construct-argument,   type: skill,     label: "Construct and defend a well-reasoned argument: claim → reasons → evidence → address counterarguments (argument mapping)", target_level: 2, bloom: create }
  - { id: A-intellectual-humility, type: ability,  label: "Intellectual humility & open-mindedness: willingness to be wrong, follow evidence, and revise beliefs", target_level: 2, affective_stage: value, assessed_occasions: 3 }
  - { id: A-skepticism-curiosity, type: ability,   label: "Skeptical curiosity: question claims and assumptions rather than accept them at face value", target_level: 2, affective_stage: respond, assessed_occasions: 3 }

atoms:
  - { id: atom-1, title: "What critical thinking is", ksa_refs: [K-reasoning], phase: 1, modalities: [{dimension: read, subtype: Article}, {dimension: watch, subtype: Video Explainer}, {dimension: see, subtype: Mental Model}, {dimension: evaluate, subtype: Pop Quiz}], rubric: knowledge-mini }
  - { id: atom-2, title: "Logical fallacies & reasoning biases", ksa_refs: [K-fallacies-biases], phase: 1, modalities: [{dimension: read, subtype: Article}, {dimension: watch, subtype: Video Explainer}, {dimension: see, subtype: Framework}, {dimension: evaluate, subtype: Pop Quiz}], rubric: knowledge-mini }
  - { id: atom-3, title: "Evaluate arguments & evidence", ksa_refs: [S-evaluate-arguments], phase: 2, modalities: [{dimension: see, subtype: Diagram}, {dimension: practice, subtype: Worksheet / Exercise}, {dimension: practice, subtype: Case Study}, {dimension: evaluate, subtype: Performance Task}], rubric: skill }
  - { id: atom-4, title: "Question & verify", ksa_refs: [S-question-verify], phase: 3, modalities: [{dimension: read, subtype: Technical Article}, {dimension: practice, subtype: Worksheet / Exercise}, {dimension: practice, subtype: AI Prompt Question}, {dimension: evaluate, subtype: Performance Task}], rubric: skill }
  - { id: atom-5, title: "Build & defend a reasoned argument", ksa_refs: [S-construct-argument, A-intellectual-humility, A-skepticism-curiosity], phase: 3, modalities: [{dimension: practice, subtype: Essay / Writing}, {dimension: practice, subtype: Simulation}, {dimension: collaborate, subtype: Discussion Forum}, {dimension: evaluate, subtype: Behavioral Assessment}], rubric: behavioral }
  - { id: atom-6, title: "Capstone: reason through a real issue", ksa_refs: [S-evaluate-arguments, S-question-verify, S-construct-argument, A-intellectual-humility, A-skepticism-curiosity], phase: 4, modalities: [{dimension: practice, subtype: Project / Quest}, {dimension: collaborate, subtype: Showcase / Demo Day}, {dimension: collaborate, subtype: Async Peer Review}, {dimension: evaluate, subtype: Capstone Project}], rubric: capstone-5 }

capstone:
  title: "Take a real, contested claim or issue, evaluate the evidence on all sides, and defend a reasoned conclusion"
  integrates_ksa: [K-reasoning, K-fallacies-biases, S-evaluate-arguments, S-question-verify, S-construct-argument, A-intellectual-humility, A-skepticism-curiosity]
  rubric: capstone-5

badge:
  name: "Critical Thinker"
  evidence_required: ["atom-3", "atom-4", "atom-5", "capstone"]
  issued_on: verified-evidence
```

---

## 🎯 Target job competency

**Think critically.** Employers want people who can cut through noise: evaluate claims, weigh evidence,
spot flawed reasoning, ask the right questions, and reach a defensible conclusion — especially now that
AI can produce fluent, confident, sometimes-wrong content at scale. It is one of the most-requested
competencies across every function. Mapped to **O\*NET** (Critical Thinking, Active Learning, Judgment
& Decision Making) and **ESCO** transversal *"think critically / analytically."*

## 🧬 KSA breakdown — a cognitive skill, taught the right way

| KSA | Component | Why this type | Target |
| --- | --------- | ------------- | ------ |
| 🧠 Knowledge | The anatomy of reasoning | A mental model: claims, premises, inference, standards | L2 |
| 🧠 Knowledge | Fallacies & reasoning biases | You can't catch flaws you can't name | L2 |
| 🛠️ Skill | Evaluate arguments & evidence | A trainable technique (deconstruct + judge) | **L2** |
| 🛠️ Skill | Question & verify | Socratic questioning + source evaluation | **L2** |
| 🛠️ Skill | Build & defend an argument | Argument mapping; address counterarguments | L2 |
| 🌱 Ability | Intellectual humility | A disposition: willingness to be wrong & revise | L2 |
| 🌱 Ability | Skeptical curiosity | A habit of questioning before accepting | L2 |

> **Why this shape:** critical thinking is mostly **doing** (Skills: evaluate, question, construct),
> but it only *works* when paired with the **Abilities** that drive it — intellectual humility (to
> follow evidence even against your own view) and skeptical curiosity (to question the obvious). Those
> Abilities are assessed **behaviorally, across ≥3 occasions**, not with a quiz.

## 📘 Learning objectives (Bloom + KSA)

| Objective | Bloom | KSA | Component | Target |
| --------- | ----- | --- | --------- | ------ |
| Explain the parts of an argument and distinguish validity from soundness | Understand | 🧠 K | K-reasoning | L2 |
| Recognize common logical fallacies and reasoning biases | Understand | 🧠 K | K-fallacies-biases | L2 |
| Deconstruct an argument and evaluate its evidence and logic | Analyze | 🛠️ S | S-evaluate-arguments | L2 |
| Ask Socratic questions and evaluate source credibility | Apply | 🛠️ S | S-question-verify | L2 |
| Construct and defend a reasoned argument addressing counterarguments | Create | 🛠️ S | S-construct-argument | L2 |
| Stay open to being wrong and revise beliefs with evidence | Value (affective) | 🌱 A | A-intellectual-humility | L2 |
| Question claims and assumptions across situations | Respond (affective) | 🌱 A | A-skepticism-curiosity | L2 |

---

## 🔍 Phase planner

| Phase | Atom(s) | KSA focus | Activity | Assessment |
| ----- | ------- | --------- | -------- | ---------- |
| 🙉 1 · hear | Atom 1, 2 | 🧠 K | reading + video on reasoning; fallacy/bias framework | knowledge-mini (pop quizzes) |
| 🙈 2 · see | Atom 3 | 🛠️ S | model argument analysis; deconstruct & judge a real case | performance task |
| 🙊 3 · do | Atom 4, 5 | 🛠️ S + 🌱 A | Socratic questioning + source audit; build & defend an argument | performance task + behavioral assessment |
| 🐵 4 · share | Atom 6 (capstone) | 🛠️ S + 🌱 A | reason through a real issue; defend + peer review | capstone-5 |

---

## 🚀 Capstone & 📊 assessment

Full brief in [`capstone.md`](capstone.md); all rubrics in [`rubrics.md`](rubrics.md). In short:
formative pop quizzes for the Knowledge atoms, skill performance tasks for argument evaluation and
questioning/verification, a **behavioral assessment** across occasions for the Abilities, and a
reasoned analysis of a real issue, defended on the standard 5-criteria capstone rubric. The badge →
skills-map mapping is in [`skills-map.md`](skills-map.md).

## 🎓 Outcomes & recognition

- A working model of reasoning that replaces "I just feel it's true" with **claims + evidence + logic**.
- The ability to **deconstruct and evaluate** any argument and its evidence.
- A toolkit to **question and verify**: Socratic questions, source evaluation, steelmanning.
- The ability to **build and defend** a reasoned position that survives counterarguments.
- The durable **intellectual humility** and **skeptical curiosity** that make it stick — evidenced over time.
- A portfolio artifact: a reasoned analysis of a real, contested issue.
- LinkedIn-compatible digital badge: **🏅 Critical Thinker** — a multiplier on almost any role.
