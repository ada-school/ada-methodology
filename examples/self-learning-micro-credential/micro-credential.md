# 🎓 Micro-Credential — Self-Learning: Learn Anything Online & with AI

The full specification for this micro-credential. It conforms to
[`../../specs/micro-credential-v2-schema.md`](../../specs/micro-credential-v2-schema.md).

---

## YAML front matter

```yaml
schema: ada-microcredential/v2
id: mc-self-learning
title: "Self-Learning: Learn Anything Online & with AI"
language: en
duration_hours: 10
level: beginner
status: published
license: CC-BY-SA-4.0
mentors: ["@sancarbar"]

target_roles:
  - role: "Any role and any learner — self-learning is the meta-skill that underpins every other credential and a lifelong career"
    framework_ref: >
      O*NET process skills: 2.A.2.a Active Learning, 2.A.2.b Learning Strategies, 2.A.2.c Critical Thinking ·
      ESCO transversal: "learn to learn", "manage one's own learning", "process information" ·
      DigComp 2.2 area 1: Information & data literacy (browsing/searching, evaluating data & information)

ksa:
  - { id: K-learning-process,    type: knowledge, label: "How learning works: the process beats the answer; struggle & productive failure; metacognition", target_level: 2, bloom: understand }
  - { id: K-sources-and-ai-limits, type: knowledge, label: "Evaluating trustworthy sources, and how LLMs work + their limitations (hallucination, no live data, bias, confidence ≠ correctness)", target_level: 2, bloom: understand }
  - { id: S-search-research,     type: skill,     label: "Research with search engines: craft queries, use operators, triangulate trustworthy sources", target_level: 2, bloom: apply, primary: true }
  - { id: S-learn-with-ai,       type: skill,     label: "Learn with AI: basic prompting to explain anything, ask for sources, and verify the output", target_level: 2, bloom: apply, primary: true }
  - { id: S-learning-loop,       type: skill,     label: "Run a self-directed learning loop: goal → resources → practice → self-test → reflect", target_level: 2, bloom: apply }
  - { id: A-curiosity,           type: ability,   label: "Curiosity & learner agency: ask questions and drive your own learning", target_level: 2, affective_stage: value, assessed_occasions: 3 }
  - { id: A-resilience-failure,  type: ability,   label: "Resilience: treat being stuck/wrong as data and persist (learn by failing forward)", target_level: 2, affective_stage: respond, assessed_occasions: 3 }

atoms:
  - { id: atom-1, title: "How learning works (process > answer)", ksa_refs: [K-learning-process], phase: 1, modalities: [{dimension: read, subtype: Article}, {dimension: watch, subtype: Video Explainer}, {dimension: see, subtype: Mental Model}, {dimension: evaluate, subtype: Pop Quiz}], rubric: knowledge-mini }
  - { id: atom-2, title: "Trustworthy sources & how AI really works", ksa_refs: [K-sources-and-ai-limits], phase: 1, modalities: [{dimension: read, subtype: Article}, {dimension: see, subtype: Framework}, {dimension: practice, subtype: Worksheet / Exercise}, {dimension: evaluate, subtype: Pop Quiz}], rubric: knowledge-mini }
  - { id: atom-3, title: "Research with search engines", ksa_refs: [S-search-research], phase: 2, modalities: [{dimension: watch, subtype: Video Explainer}, {dimension: see, subtype: Diagram}, {dimension: practice, subtype: Challenge / Quest}, {dimension: evaluate, subtype: Performance Task}], rubric: skill }
  - { id: atom-4, title: "Learn with AI (basic prompting + verify)", ksa_refs: [S-learn-with-ai, K-sources-and-ai-limits], phase: 3, modalities: [{dimension: read, subtype: Technical Article}, {dimension: practice, subtype: AI Prompt Question}, {dimension: practice, subtype: Worksheet / Exercise}, {dimension: evaluate, subtype: Performance Task}], rubric: skill }
  - { id: atom-5, title: "The self-learning loop (learn by failing forward)", ksa_refs: [S-learning-loop, A-curiosity, A-resilience-failure], phase: 3, modalities: [{dimension: practice, subtype: Project / Quest}, {dimension: practice, subtype: Reflection / Learning Log}, {dimension: collaborate, subtype: Pair Programming}, {dimension: evaluate, subtype: Behavioral Assessment}], rubric: behavioral }
  - { id: atom-6, title: "Capstone: teach yourself something new & teach it back", ksa_refs: [S-search-research, S-learn-with-ai, S-learning-loop, A-curiosity, A-resilience-failure], phase: 4, modalities: [{dimension: practice, subtype: Project / Quest}, {dimension: collaborate, subtype: Showcase / Demo Day}, {dimension: collaborate, subtype: Async Peer Review}, {dimension: evaluate, subtype: Capstone Project}], rubric: capstone-5 }

capstone:
  title: "Teach yourself a new micro-skill using online + AI + search, document the process (incl. failures), and teach it back"
  integrates_ksa: [K-learning-process, K-sources-and-ai-limits, S-search-research, S-learn-with-ai, S-learning-loop, A-curiosity, A-resilience-failure]
  rubric: capstone-5

badge:
  name: "Self-Directed Learner"
  evidence_required: ["atom-3", "atom-4", "atom-5", "capstone"]
  issued_on: verified-evidence
```

---

## 🎯 Target job competency

**Learn independently and continuously.** Employers increasingly hire for *learning agility* — the
capacity to pick up new tools, domains, and problems without being formally taught. This credential
makes that hireable: the learner can find trustworthy answers online, use AI as a study partner
(without being misled by it), and run a disciplined self-learning loop. Mapped to **O\*NET** process
skills (Active Learning, Learning Strategies, Critical Thinking), **ESCO** *"learn to learn"*, and
**DigComp** area 1 (information & data literacy).

## 🧬 KSA breakdown — the meta-skill, taught the right way

| KSA | Component | Why this type | Target |
| --- | --------- | ------------- | ------ |
| 🧠 Knowledge | How learning works (process > answer; productive failure) | A mental model that reframes struggle as learning | L2 |
| 🧠 Knowledge | Trustworthy sources & LLM limits | You can't verify what you don't understand | L2 |
| 🛠️ Skill | Research with search engines | A trainable technique (queries, operators, triangulation) | **L2** |
| 🛠️ Skill | Learn with AI (+ verify) | Basic prompting *paired with* verification | **L2** |
| 🛠️ Skill | The self-learning loop | A repeatable procedure for any new topic | L2 |
| 🌱 Ability | Curiosity & learner agency | A disposition shown across situations, over time | L2 |
| 🌱 Ability | Resilience (learn by failing) | A habit of persisting through being stuck/wrong | L2 |

> **Why this shape:** self-learning is mostly **doing** (Skills: search, prompt, loop), but it only
> *sticks* when paired with the **Abilities** that drive it — curiosity (to keep asking) and
> resilience (to keep going when you fail). Those Abilities are assessed **behaviorally, across ≥3
> occasions**, never with a quiz.

## 📘 Learning objectives (Bloom + KSA)

| Objective | Bloom | KSA | Component | Target |
| --------- | ----- | --- | --------- | ------ |
| Explain why the *process* of reaching an answer matters more than the answer, and how failure aids learning | Understand | 🧠 K | K-learning-process | L2 |
| Evaluate whether a source is trustworthy and explain basic LLM limitations | Understand/Evaluate | 🧠 K | K-sources-and-ai-limits | L2 |
| Find and triangulate trustworthy answers using a search engine | Apply | 🛠️ S | S-search-research | L2 |
| Prompt an AI to explain a topic, request sources, and verify the result | Apply | 🛠️ S | S-learn-with-ai | L2 |
| Run a full self-learning loop on a chosen topic | Apply | 🛠️ S | S-learning-loop | L2 |
| Drive your own learning with curiosity across multiple situations | Value (affective) | 🌱 A | A-curiosity | L2 |
| Persist and adapt when stuck or wrong, treating failure as data | Respond (affective) | 🌱 A | A-resilience-failure | L2 |

---

## 🔍 Phase planner

| Phase | Atom(s) | KSA focus | Activity | Assessment |
| ----- | ------- | --------- | -------- | ---------- |
| 🙉 1 · hear | Atom 1, 2 | 🧠 K | reading + video on how learning works; source-trust + LLM-limits worksheet | knowledge-mini (pop quizzes) |
| 🙈 2 · see | Atom 3 | 🛠️ S | search techniques modeled; a research scavenger hunt | performance task |
| 🙊 3 · do | Atom 4, 5 | 🛠️ S + 🌱 A | AI study prompts + verification; a real learn-by-failing micro-project | performance task + behavioral assessment |
| 🐵 4 · share | Atom 6 (capstone) | 🛠️ S + 🌱 A | teach yourself a new skill; document the messy middle; teach back | capstone-5 |

---

## 🚀 Capstone & 📊 assessment

Full brief in [`capstone.md`](capstone.md); all rubrics in [`rubrics.md`](rubrics.md). In short:
formative pop quizzes for the Knowledge atoms, a skill performance task for search and for AI-assisted
learning, a **behavioral assessment** across occasions for the Abilities, and a self-taught skill +
learning log + teach-back graded on the standard 5-criteria capstone rubric. The badge → skills-map
mapping is in [`skills-map.md`](skills-map.md).

## 🎓 Outcomes & recognition

- A reframed relationship with effort and failure: **struggle is learning**, not a sign you're failing.
- The ability to **find trustworthy answers** online and **triangulate** them.
- The ability to **learn with AI** as a study partner — and to catch it when it's wrong.
- A repeatable **self-learning loop** you can point at any new skill.
- A portfolio artifact: a self-taught micro-skill + a learning log that shows the *process* (including
  the failures and how you recovered).
- LinkedIn-compatible digital badge: **🏅 Self-Directed Learner** — the meta-credential that makes
  every other pathway faster.
