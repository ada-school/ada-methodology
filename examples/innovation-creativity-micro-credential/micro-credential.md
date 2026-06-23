# 🎓 Micro-Credential — Innovation & Creativity: From Idea to Value

The full specification for this micro-credential. It conforms to
[`../../specs/micro-credential-v2-schema.md`](../../specs/micro-credential-v2-schema.md).

---

## YAML front matter

```yaml
schema: ada-microcredential/v2
id: mc-innovation-creativity
title: "Innovation & Creativity: From Idea to Value"
language: en
duration_hours: 12
level: beginner
status: published
license: CC-BY-SA-4.0
mentors: ["@sancarbar"]

target_roles:
  - role: "Any role that must improve products, services, or processes — PMs, designers, founders, marketers, engineers, operations, strategy"
    framework_ref: >
      O*NET abilities: 1.A.1.b.1 Fluency of Ideas, 1.A.1.b.2 Originality; work activities 4.A.2.b.1 Thinking Creatively;
      work styles: Innovation · ESCO transversal: "think creatively", "use creativity", "develop creative ideas"

ksa:
  - { id: K-creativity-innovation, type: knowledge, label: "What creativity and innovation are: divergent vs. convergent thinking; innovation = creativity + execution that creates value; common idea myths", target_level: 2, bloom: understand }
  - { id: K-ideation-frameworks,   type: knowledge, label: "Ideation frameworks and where they fit: design thinking, SCAMPER, lateral thinking, analogies, constraints, brainwriting", target_level: 2, bloom: understand }
  - { id: S-reframe-opportunities, type: skill,     label: "Reframe a problem and spot opportunities: observe users, find insights, write sharp 'How Might We' questions", target_level: 2, bloom: analyze, primary: true }
  - { id: S-generate-ideas,        type: skill,     label: "Generate many varied ideas on demand (fluency, flexibility, originality) using divergent techniques", target_level: 2, bloom: create, primary: true }
  - { id: S-develop-prototype,     type: skill,     label: "Develop, prototype and evaluate ideas: converge with criteria, build a rough prototype, test and iterate", target_level: 2, bloom: create }
  - { id: A-creative-confidence,   type: ability,   label: "Creative confidence & productive risk-taking: share half-formed ideas, embrace failure as iteration, defer judgment", target_level: 2, affective_stage: value, assessed_occasions: 3 }
  - { id: A-curiosity-openness,    type: ability,   label: "Curiosity & openness: seek novelty, ask 'what if', and connect ideas across domains", target_level: 2, affective_stage: respond, assessed_occasions: 3 }

atoms:
  - { id: atom-1, title: "What creativity & innovation are", ksa_refs: [K-creativity-innovation], phase: 1, modalities: [{dimension: read, subtype: Article}, {dimension: watch, subtype: Video Explainer}, {dimension: see, subtype: Mental Model}, {dimension: evaluate, subtype: Pop Quiz}], rubric: knowledge-mini }
  - { id: atom-2, title: "Ideation frameworks", ksa_refs: [K-ideation-frameworks], phase: 1, modalities: [{dimension: read, subtype: Article}, {dimension: watch, subtype: Video Explainer}, {dimension: see, subtype: Framework}, {dimension: evaluate, subtype: Pop Quiz}], rubric: knowledge-mini }
  - { id: atom-3, title: "Reframe problems & spot opportunities", ksa_refs: [S-reframe-opportunities], phase: 2, modalities: [{dimension: see, subtype: Diagram}, {dimension: practice, subtype: Worksheet / Exercise}, {dimension: practice, subtype: Case Study}, {dimension: evaluate, subtype: Performance Task}], rubric: skill }
  - { id: atom-4, title: "Generate ideas", ksa_refs: [S-generate-ideas], phase: 3, modalities: [{dimension: read, subtype: Technical Article}, {dimension: practice, subtype: Worksheet / Exercise}, {dimension: practice, subtype: AI Prompt Question}, {dimension: evaluate, subtype: Performance Task}], rubric: skill }
  - { id: atom-5, title: "Develop, prototype & evaluate", ksa_refs: [S-develop-prototype, A-creative-confidence, A-curiosity-openness], phase: 3, modalities: [{dimension: practice, subtype: Lab / Build}, {dimension: practice, subtype: Simulation}, {dimension: collaborate, subtype: Discussion Forum}, {dimension: evaluate, subtype: Behavioral Assessment}], rubric: behavioral }
  - { id: atom-6, title: "Capstone: innovation challenge", ksa_refs: [S-reframe-opportunities, S-generate-ideas, S-develop-prototype, A-creative-confidence, A-curiosity-openness], phase: 4, modalities: [{dimension: practice, subtype: Project / Quest}, {dimension: collaborate, subtype: Showcase / Demo Day}, {dimension: collaborate, subtype: Async Peer Review}, {dimension: evaluate, subtype: Capstone Project}], rubric: capstone-5 }

capstone:
  title: "Run a full innovation challenge: reframe a real problem, generate options, prototype the best, and pitch it"
  integrates_ksa: [K-creativity-innovation, K-ideation-frameworks, S-reframe-opportunities, S-generate-ideas, S-develop-prototype, A-creative-confidence, A-curiosity-openness]
  rubric: capstone-5

badge:
  name: "Creative Innovator"
  evidence_required: ["atom-3", "atom-4", "atom-5", "capstone"]
  issued_on: verified-evidence
```

---

## 🎯 Target job competency

**Think creatively and innovate.** Organizations don't just want novel ideas — they want people who can
**reframe problems, generate options, and turn the best into something real and valuable.** As routine
work is automated, the premium shifts to originality, idea fluency, and the judgment to develop ideas
into impact. Mapped to **O\*NET** (Fluency of Ideas, Originality, Thinking Creatively, Innovation) and
**ESCO** transversal *"think creatively / use creativity."*

## 🧬 KSA breakdown — a creative skill, taught the right way

| KSA | Component | Why this type | Target |
| --- | --------- | ------------- | ------ |
| 🧠 Knowledge | What creativity & innovation are | A mental model: divergent/convergent; idea → value | L2 |
| 🧠 Knowledge | Ideation frameworks | You can't apply tools you don't know | L2 |
| 🛠️ Skill | Reframe & spot opportunities | A trainable technique (observe → insight → HMW) | **L2** |
| 🛠️ Skill | Generate ideas | Divergent thinking on demand (fluency/flexibility/originality) | **L2** |
| 🛠️ Skill | Develop, prototype & evaluate | Converge, prototype, test, iterate | L2 |
| 🌱 Ability | Creative confidence | A disposition: share rough ideas, embrace failure | L2 |
| 🌱 Ability | Curious openness | A habit: seek novelty, connect across domains | L2 |

> **Why this shape:** creativity is mostly **doing** (Skills: reframe, generate, develop), but it only
> *flows* when paired with the **Abilities** that unlock it — **creative confidence** (the belief and
> willingness to share imperfect ideas and treat failure as iteration) and **curious openness** (the
> habit of seeking novelty and connecting distant ideas). Those Abilities are assessed **behaviorally,
> across ≥3 occasions**, not with a quiz.

## 📘 Learning objectives (Bloom + KSA)

| Objective | Bloom | KSA | Component | Target |
| --------- | ----- | --- | --------- | ------ |
| Explain divergent vs. convergent thinking and how creativity becomes innovation | Understand | 🧠 K | K-creativity-innovation | L2 |
| Describe major ideation frameworks and when to use each | Understand | 🧠 K | K-ideation-frameworks | L2 |
| Reframe a problem and write sharp opportunity ("How Might We") questions | Analyze | 🛠️ S | S-reframe-opportunities | L2 |
| Generate many varied, original ideas on demand | Create | 🛠️ S | S-generate-ideas | L2 |
| Develop, prototype, and evaluate ideas against criteria | Create | 🛠️ S | S-develop-prototype | L2 |
| Share rough ideas and treat failure as iteration | Value (affective) | 🌱 A | A-creative-confidence | L2 |
| Seek novelty and connect ideas across domains | Respond (affective) | 🌱 A | A-curiosity-openness | L2 |

---

## 🔍 Phase planner

| Phase | Atom(s) | KSA focus | Activity | Assessment |
| ----- | ------- | --------- | -------- | ---------- |
| 🙉 1 · hear | Atom 1, 2 | 🧠 K | reading + video on creativity/innovation; ideation frameworks | knowledge-mini (pop quizzes) |
| 🙈 2 · see | Atom 3 | 🛠️ S | model a reframe; observe → insight → "How Might We" | performance task |
| 🙊 3 · do | Atom 4, 5 | 🛠️ S + 🌱 A | divergent idea sprints; prototype + evaluate the best | performance task + behavioral assessment |
| 🐵 4 · share | Atom 6 (capstone) | 🛠️ S + 🌱 A | full innovation challenge; pitch + peer review | capstone-5 |

---

## 🚀 Capstone & 📊 assessment

Full brief in [`capstone.md`](capstone.md); all rubrics in [`rubrics.md`](rubrics.md). In short:
formative pop quizzes for the Knowledge atoms, skill performance tasks for reframing and idea
generation, a **behavioral assessment** across occasions for the Abilities, and a full
reframe→ideate→prototype→pitch challenge scored on the standard 5-criteria capstone rubric. The badge →
skills-map mapping is in [`skills-map.md`](skills-map.md).

## 🎓 Outcomes & recognition

- A working model of creativity that replaces "I'm just not creative" with **a repeatable process**.
- The ability to **reframe** a problem into sharp opportunity questions.
- On-demand **idea fluency** — generate many varied, original options without freezing.
- The ability to **develop, prototype, and evaluate** ideas down to one you can pitch.
- The durable **creative confidence** and **curious openness** that make it stick — evidenced over time.
- A portfolio artifact: a documented innovation challenge with a prototype and pitch.
- LinkedIn-compatible digital badge: **🏅 Creative Innovator** — a signal for product, design & strategy roles.
