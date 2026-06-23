# CLAUDE.md

Guidance for AI agents (Claude, Cursor, and other Gen AI assistants) working in this
repository. Read this first before creating or editing content.

---

## 1. What this repository is

This repo holds the **ADA Methodology (Applied Digital Apprenticeship)** — an open,
CC BY-SA 4.0 instructional-design framework created by [Ada School](https://ada-school.org/)
to develop **job-ready digital talent**.

It is **a documentation / curriculum-design repository, not a software project.** There is
no build step, no dependencies, no test suite. The "source code" is Markdown: methodology
docs, reusable templates, designer guides, and worked examples, maintained in three
languages.

The core idea: learning is packaged as **micro-credentials** (10–30h job-ready units),
each made of **learning atoms** (the smallest instructional unit), sequenced through
**4 learning phases** modeled on the Confucius progression *hear → see → do → share*.

This repo is being extended to a **v2** that adds the **KSA framework
(Knowledge, Skills, Abilities)** and a **skills-map → job-matching** model, with a
**Gen AI authoring workflow**. The specifications for v2 live in [`specs/`](specs/).

---

## 2. Repository map

```
ada-methodology/
├── README.md            # English methodology (canonical / source of truth)
├── README-ES.md         # Spanish translation
├── README-PT-BR.md      # Portuguese (Brazil) translation
├── LEARN.md             # Self-paced course: master ADA by building a credential (EN)
├── CONTRIBUTING.md      # Contribution rules + license
├── CLAUDE.md            # ← you are here
├── LICENSE              # CC BY-SA 4.0
├── index.html           # Self-contained interactive docs browser (generated)
├── build-index.py       # Generator: embeds all Markdown + assets into index.html
├── guides/              # Step-by-step designer manuals (EN/ES)
├── templates/           # Reusable, copy-to-create templates
│   ├── *.md             # English templates
│   ├── es/              # Spanish templates
│   └── pt-br/           # Portuguese templates
├── examples/            # Worked, end-to-end examples (incl. full courses with their own
│   │                    #   build-course.py + course.html):
│   ├── growth-mindset-micro-credential/      # full Ability course (atoms, rubrics, images)
│   ├── python-variables-micro-credential/    # full technical Skill course (atoms + labs/tests)
│   ├── ada-methodology-designer-micro-credential/  # train-the-designer course (packaged LEARN.md)
│   ├── effective-communication-micro-credential/   # full human-skill course (S + A, role-plays)
│   ├── self-learning-micro-credential/             # full meta-skill course (learn online + with AI)
│   ├── problem-solving-micro-credential/           # full cognitive-skill course (define/diagnose/decide)
│   ├── critical-thinking-micro-credential/         # full cognitive-skill course (reason/evaluate/defend)
│   └── innovation-creativity-micro-credential/     # full creative-skill course (reframe/ideate/prototype)
├── specs/               # v2 specifications (KSA, skills map, Gen AI authoring)
└── img/                 # Images used in docs
```

### Key concepts to know

| Concept              | Definition                                                                 |
| -------------------- | -------------------------------------------------------------------------- |
| **Learning Atom**    | Smallest unit; one objective; 7 modalities `Read · Listen · Watch · See · Practice · Evaluate · Collaborate` (full sub-type map in [`specs/learning-atom-topology.md`](specs/learning-atom-topology.md)). |
| **Micro-credential** | 10–30h unit; 4–8 atoms; capstone + rubric + digital badge.                 |
| **4 Phases**         | 🙉 Self-Guided Intro → 🙈 Visual Exploration → 🙊 Applied Practice → 🐵 Collaboration & Reflection. |
| **Bloom alignment**  | Objectives use Bloom verbs (Remember → … → Create).                        |
| **KSA (v2)**         | Knowledge (know-what/why), Skills (know-how), Abilities (durable/human/attitudes). |
| **Skills map (v2)**  | Graph of KSA components a learner earns, matched against a job's minimums.  |
| **Role deconstruction (v2)** | Process to turn a real role into duties → tasks → KSA (at a high-performer bar) → a sequenced micro-credential **pathway** ([`specs/role-to-credential-mapping.md`](specs/role-to-credential-mapping.md)). |
| **Onboarding course** | [`LEARN.md`](LEARN.md) is a self-referential micro-credential that teaches the methodology *by building one* (KSA · Bloom · topology → a full ADA credential). Point new authors here first. |

---

## 3. Conventions (follow these when editing)

- **Language & tone:** clear, professional, inclusive. Action-oriented and practical.
- **Markdown style mirrors existing files:**
  - Section emoji headers are used intentionally (e.g. `## 🎯`, `## ⚛`). Match the
    surrounding file's style rather than imposing a new one.
  - Use tables for rubrics, mappings, and planners.
  - Use task-list checkboxes (`- [ ]`) for checklists and prerequisites.
  - Templates use `[instructions in brackets]` as fill-in placeholders.
- **Frameworks:** when defining a competency, link it to a recognized standard —
  **SFIA, O\*NET, ESCO, or ILO** — exactly as existing docs do.
- **Trilingual rule:** `README.md` (English) is the **canonical source of truth**.
  - When you change methodology substance in `README.md`, note that `README-ES.md` and
    `README-PT-BR.md` (and the `templates/es/`, `templates/pt-br/` mirrors) should be
    updated to match. Do **not** silently let translations drift.
  - Keep section structure parallel across the three languages.
- **Interactive site (`index.html`):** a generated, self-contained browser of the repo.
  Regenerate it with `python3 build-index.py` after changing docs. Its UI chrome is
  translatable via a small JSON string map (`I18N` in `build-index.py`) with an **EN / ES / PT
  language switcher**; keep those keys in sync when you add UI text. The header uses the
  spinning `img/Isotipo.png` mark. Note: v2 `specs/` are English-only (canonical).
  - **Translations are not duplicated in the nav.** `README-ES/PT-BR` and the `templates/es`,
    `templates/pt-br` mirrors are hidden from the sidebar/search; the language button swaps
    them in place for the doc you're viewing. The canonical→translation mapping lives in
    `TRANSLATION_PAIRS` in `build-index.py` — **add any new translated doc there** so the
    switcher (not a duplicate nav entry) handles it.
- **Licensing:** all content is **CC BY-SA 4.0**. Cite sources; only use external content
  with proper permission; attribute Ada School.
- **Links:** prefer relative links between repo files (e.g. `templates/learning-atom-template.md`).
- **Brand identity (use consistently in visuals, `index.html`, diagrams):**

  | Role | Name | Hex | Usage rule |
  | ---- | ---- | --- | ---------- |
  | Primary · governs + text | **Indigo** | `#1E2A6E` | Trust + knowledge. Use for **text/headlines on light**. |
  | Accent · signature | **Turquoise** | `#15B5C6` | Heritage. **Fill or accent only — never text on light** (text on dark is OK). |
  | Accent · achievement | **Gold** | `#E0A53C` | Achievement/credential. **≤1 use per piece**. Fill, or headline **on dark**. |
  | Ink · dark base | **Ink** | `#0A1124` | Dark backgrounds / base. |

  - **Logo:** `img/ada-school-logo.png` (Ada Lovelace mark). Keep clear space; don't recolor.
  - Reserve **Gold** for achievement/credential/badge cues only.
- **Images:** store in `img/` with **kebab-case, space-free** filenames (Markdown/HTML links
  break on spaces). Key assets: `ada-methodology-overview.png`,
  `ada-learning-atom-structure.png`, `ada-school-logo.png`, and `Isotipo.png` (the circular
  Ada Lovelace mark — used as the spinning app/menu icon and favicon in `index.html`).

---

## 4. How to create new content

1. **Start from a template** in `templates/` — never hand-roll structure.
   - New atom → `templates/learning-atom-template.md`
   - New micro-credential → `templates/micro-credential-ada-template.md`
   - New codelab → `templates/codelab-ada-template.md`
   - New v2 (KSA-aware) micro-credential → `specs/micro-credential-v2-schema.md`
   - Whole **role/job → pathway** of micro-credentials → follow
     [`specs/role-to-credential-mapping.md`](specs/role-to-credential-mapping.md) (triangulate
     frameworks + postings + high-performer observation; AI proposes, humans validate).
2. **Anchor to a real job competency** and link it to SFIA/O\*NET/ESCO/ILO.
3. **Write Bloom-aligned objectives** (measurable verbs).
4. **(v2) Tag each objective/atom with its KSA type** (K / S / A) — see
   [`specs/ksa-taxonomy.md`](specs/ksa-taxonomy.md).
5. **Design 4–8 atoms**, each with Concept → Example → Practice → Evaluation. Pick concrete
   modality sub-types from [`specs/learning-atom-topology.md`](specs/learning-atom-topology.md)
   that match the atom's KSA type.
6. **Add a capstone + rubric** (mini-rubric for atoms, 5-criteria rubric for capstone).
7. **Include collaborative/human elements** (mentor sessions, peer review, showcase).
8. **Validate** against the checklist in `guides/curriculum-design-guide.md`.

### Authoring with Gen AI

The end-to-end "prompt → micro-credential" workflow (job posting in → skills map +
atoms + rubrics out) is specified in
[`specs/genai-authoring-workflow.md`](specs/genai-authoring-workflow.md). Use that spec's
prompts and JSON schemas so generated output stays structurally consistent and reviewable.

---

## 5. Guardrails

- **Do not** invent certifications, accreditations, or partnerships that aren't documented.
- **Do not** present AI-generated competency mappings as authoritative without flagging
  them for human (mentor/employer) validation — the methodology requires a human-in-the-loop.
- **Do not** break the trilingual parallelism or drop the framework citations.
- **Do not** add build tooling, package files, or code dependencies — this is a docs repo.
- **Keep examples portfolio-ready and realistic**: prefer free/accessible tools.
- **Preserve the existing structure** when extending; v2 should *layer onto* v1, not
  replace it.

---

## 6. Commit / PR conventions

- Commit messages in this repo are short and descriptive (e.g.
  `docs: add curriculum design guide`, `Updated spanish version.`). Match that style.
- Only commit when explicitly asked.
- Group related content changes; when methodology substance changes, mention translation
  follow-ups needed.
