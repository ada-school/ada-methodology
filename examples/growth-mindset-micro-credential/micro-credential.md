# 🎓 Micro-Credential — Growth Mindset for High-Performing Professionals

The full specification for this micro-credential. It conforms to
[`../../specs/micro-credential-v2-schema.md`](../../specs/micro-credential-v2-schema.md).

---

## YAML front matter

```yaml
schema: ada-microcredential/v2
id: mc-growth-mindset-pro
title: "Growth Mindset for High-Performing Professionals"
language: en
duration_hours: 16
status: published
license: CC-BY-SA-4.0
mentors: ["@sancarbar"]

target_roles:
  - role: "Any role in a fast-changing, learning-intensive digital team"
    framework_ref: >
      O*NET Work Styles: Adaptability/Flexibility, Persistence, Achievement/Effort ·
      ESCO transversal attitudes (maintaining a growth mindset, coping with uncertainty) ·
      SFIA: LEDA (learning & development), behavioural factors (autonomy, complexity)

ksa:
  - { id: K-mindset-science, type: knowledge, label: "Fixed vs. growth mindset; neuroplasticity; what research does and doesn't claim", target_level: 1, bloom: understand }
  - { id: K-mindset-nuance,  type: knowledge, label: "False growth mindset; effect-size nuance; when mindset matters most", target_level: 1, bloom: understand }
  - { id: S-yet-reframe,     type: skill,     label: "Apply a 'power of yet' reframing move to a real setback", target_level: 2, bloom: apply }
  - { id: S-deliberate-practice, type: skill, label: "Design and run a deliberate-practice loop with feedback", target_level: 2, bloom: apply }
  - { id: A-growth-mindset,  type: ability,   label: "Treat failure as learning; seek challenge & feedback; persist", target_level: 3, primary: true, affective_stage: organize, assessed_occasions: 5 }
  - { id: A-adaptability,    type: ability,   label: "Stay effective and keep learning amid change/ambiguity", target_level: 2, affective_stage: value, assessed_occasions: 3 }

atoms:
  - { id: atom-1, title: "The science of mindset", ksa_refs: [K-mindset-science], phase: 1, modalities: [{dimension: read, subtype: Article}, {dimension: watch, subtype: Video Explainer}, {dimension: see, subtype: Infographic}, {dimension: evaluate, subtype: Pop Quiz}], rubric: knowledge-mini }
  - { id: atom-2, title: "Myths & nuance", ksa_refs: [K-mindset-science, K-mindset-nuance], phase: 2, modalities: [{dimension: read, subtype: Scientific Paper}, {dimension: read, subtype: Case Study}, {dimension: watch, subtype: Short}, {dimension: evaluate, subtype: AI QA Check}], rubric: knowledge-mini }
  - { id: atom-3, title: "The power of yet", ksa_refs: [S-yet-reframe, A-growth-mindset], phase: 2, modalities: [{dimension: see, subtype: Mental Model}, {dimension: watch, subtype: Tutorial / Screencast}, {dimension: practice, subtype: Worksheet / Exercise}, {dimension: evaluate, subtype: Mini-Rubric}], rubric: skill }
  - { id: atom-4, title: "Deliberate-practice lab", ksa_refs: [S-deliberate-practice, A-growth-mindset], phase: 3, modalities: [{dimension: read, subtype: Technical Article}, {dimension: practice, subtype: Lab}, {dimension: collaborate, subtype: Pair Programming}, {dimension: evaluate, subtype: Performance Task}], rubric: skill }
  - { id: atom-5, title: "Failure résumé & feedback seeking", ksa_refs: [A-growth-mindset, A-adaptability], phase: 3, modalities: [{dimension: practice, subtype: Project Task}, {dimension: collaborate, subtype: Study Group}, {dimension: evaluate, subtype: Behavioral Assessment}], rubric: ability-behavioral }
  - { id: atom-6, title: "Growth in the wild (21-day challenge)", ksa_refs: [A-growth-mindset, A-adaptability], phase: 4, modalities: [{dimension: practice, subtype: Project Task}, {dimension: read, subtype: Journal / Diary}, {dimension: collaborate, subtype: Showcase / Demo Day}, {dimension: evaluate, subtype: Behavioral Assessment}], rubric: ability-behavioral }

capstone:
  title: "Growth in the wild — a 21-day stretch challenge"
  integrates_ksa: [K-mindset-science, K-mindset-nuance, S-yet-reframe, S-deliberate-practice, A-growth-mindset, A-adaptability]
  rubric: capstone-5

badge:
  name: "Growth Mindset Practitioner"
  evidence_required: ["atom-3", "atom-4", "atom-5", "capstone"]
  issued_on: verified-evidence
```

---

## 🎯 Target job competency

Keep learning and stay effective when **goals, tools, or feedback are hard** — written in
postings as *growth mindset, learning agility, coachable, resilient, thrives on feedback*.
Mapped to **O\*NET Work Styles** (Adaptability/Flexibility, Persistence, Achievement/Effort),
**ESCO** transversal attitudes, and **SFIA** behavioural factors + *LEDA*.

## 🧬 KSA breakdown — an attitude made trainable

| KSA | Component | Why this type | Target |
| --- | --------- | ------------- | ------ |
| 🧠 Knowledge | Mindset science (fixed vs. growth, neuroplasticity) | Concepts to understand — a small enabling base | L1 |
| 🧠 Knowledge | Myths & nuance (false growth mindset, effect sizes) | Prevents shallow / performative adoption | L1 |
| 🛠️ Skill | The *power of yet* reframing move | A concrete, repeatable move you can practice | L2 |
| 🛠️ Skill | Deliberate-practice loop with feedback | A teachable method that *operationalizes* the mindset | L2 |
| 🌱 Ability | **Growth mindset** (failure = learning) | A disposition proven by behavior over time | **L3** |
| 🌱 Ability | Adaptability amid change | Cross-cutting disposition, reinforced throughout | L2 |

> **Why this shape:** you can't lecture an attitude into existence. v2 gives a light
> **Knowledge** base, two concrete **Skills** the learner can actually *do*, and then grows
> the **Ability** through repeated, authentic challenge — because dispositions are evidenced by
> *behavior across occasions*, not by a test.

## 📘 Learning objectives (Bloom + Affective + KSA)

| Objective | Bloom / Affective | KSA | Component | Target |
| --------- | ----------------- | --- | --------- | ------ |
| Explain fixed vs. growth mindset and the neuroscience behind it | Understand | 🧠 K | K-mindset-science | L1 |
| Distinguish real growth mindset from *false* growth mindset | Understand / Analyze | 🧠 K | K-mindset-nuance | L1 |
| Apply a *power of yet* reframing move to a live setback | Apply | 🛠️ S | S-yet-reframe | L2 |
| Design and run a deliberate-practice loop with feedback | Apply / Create | 🛠️ S | S-deliberate-practice | L2 |
| Treat failure as data; seek challenge and feedback; persist | Organize (affective) | 🌱 A | A-growth-mindset | L3 |
| Stay effective and keep learning when conditions change | Value (affective) | 🌱 A | A-adaptability | L2 |

---

## 🔍 Phase planner

| Phase | Atom(s) | KSA focus | Activity | Assessment |
| ----- | ------- | --------- | -------- | ---------- |
| 🙉 1 · hear | Atom 1 | 🧠 K | mindset readings + Dweck TED + infographic | knowledge-mini (pop quiz) |
| 🙈 2 · see | Atom 2, Atom 3 | 🧠 K → 🛠️ S | evidence + cases; learn the *yet* reframe | knowledge-mini + skill mini-rubric |
| 🙊 3 · do | Atom 4, Atom 5 | 🛠️ S + 🌱 A | deliberate-practice lab; failure résumé | performance + behavioral |
| 🐵 4 · share | Atom 6 (capstone) | 🌱 A | 21-day challenge + journal + peer 360 + showcase | behavioral + capstone-5 |

---

## 🚀 Capstone & 📊 assessment

Full brief in [`capstone.md`](capstone.md); all rubrics in [`rubrics.md`](rubrics.md). In short:
formative checks per atom, a behavioral rubric across **5 occasions**, and a capstone graded on
the standard 5-criteria rubric. The badge → skills-map mapping is in
[`skills-map.md`](skills-map.md).

## 🎓 Outcomes & recognition

- Conceptual mastery of mindset science **and its limits** (no hype).
- Two job-ready moves: a reframing technique and a deliberate-practice loop.
- A portfolio artifact (21-day growth log + showcase) proving the Ability.
- LinkedIn-compatible digital badge: **🏅 Growth Mindset Practitioner**.
