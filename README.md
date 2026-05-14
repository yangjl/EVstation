# Volt & Go — EV Charging Station Business Plan
## Lincoln, Nebraska

A public EV charging station positioned near the I-80 corridor and Lincoln's high-end apartment communities, offering 10 charging ports (8 Level 2 + 2 DC Fast Chargers) with a $1M total investment.

## Business Plan Snapshot

- **Business name:** Volt & Go Lincoln (placeholder — pending brand decision)
- **Target customer:** Highway travelers on I-80, EV-owning residents of high-end apartments, and local commuters without home charging access
- **Market / sector:** Electric vehicle (EV) charging infrastructure, Lincoln NE
- **Business model:** Pay-per-use charging revenue ($/kWh), optional monthly membership passes, ancillary retail/advertising revenue
- **Primary evidence sources:** AFDC station locator, Nebraska EV registration data, NEVI program allocations, Lincoln city EV plans, comparable station financial benchmarks
- **Main outputs:** Business plan docs, financial model, investor pitch deck (HTML-PPT)
- **Current phase:** Planning

## Required Project Metadata

- Project lead: [Owner name — human to fill in]
- Business or venture name: Volt & Go Lincoln (working title)
- Target customer or buyer: Highway travelers on I-80, high-end apartment EV owners, local commuters
- Market or sector: EV charging infrastructure — Lincoln, NE MSA
- Business model: Pay-per-use ($/kWh) + optional monthly membership; possible advertising/retail co-tenancy
- Data or source steward: [Owner name — human to fill in]
- Planning stage: Initial planning — assumptions drafted, awaiting human review
- Expected deliverables: Business plan docs, 5-year financial model, investor pitch deck
- Review status: Draft — human review needed before investor use

## Human Review Checkpoints

Pause for human review before changing or finalizing:

- market sizing assumptions
- customer segmentation
- competitive positioning
- pricing, revenue, cost, margin, or growth assumptions
- go-to-market strategy
- funding asks or investor-facing claims
- legal, regulatory, medical, tax, or financial claims
- interpretation of customer discovery evidence

## Reporting With HTML-PPT

Presentation reporting should use the HTML-PPT skill:

The template assumes the skill is installed at the user level. If it is missing, install it with the command documented by the skill repository:

```bash
npx skills add https://github.com/lewislulu/html-ppt-skill
```

Use source decks in `presentations/` and rendered or shared outputs in `reports/`.

When authoring decks:

- start from an existing HTML-PPT template or layout
- use token-based themes rather than hard-coded colors
- include speaker notes for human review
- record major narrative or deck-structure decisions in `doc/DECISIONS.md`

The pitch deck plan lives in `doc/PITCH_DECK_PLAN.md`.

## Hosted Landing Page (Vercel)

The repository root contains a landing page (`index.html`) that links to every site-scenario deck. It is deployed from the repo root on Vercel using `vercel.json` for clean URL rewrites.

| URL | Serves |
|---|---|
| `/` | Landing page · cards for each scenario |
| `/north` | Fallbrook / North Lincoln deck (`presentations/investor/volt-go-lincoln/`) |
| `/north/map` | Fallbrook site map |
| `/south` | SouthPointe / South Lincoln deck (`presentations/investor/volt-go-south-lincoln/`) |
| `/south/map` | SouthPointe site map |

### Vercel project settings

- **Root Directory:** repository root (leave default)
- **Framework Preset:** Other
- **Build Command:** leave empty
- **Output Directory:** `.`
- **Install Command:** leave empty

### Adding a new site scenario

1. Create a new deck folder under `presentations/investor/volt-go-<site>/` with its own `index.html` and optional `map.html` (copy one of the existing decks as a starting point).
2. Add a rewrite block to the root `vercel.json` for the new path prefix (e.g. `/east` → `presentations/investor/volt-go-east-lincoln/`).
3. Replace one of the `.scenario.placeholder` cards in `index.html` with a fully-populated scenario card pointing at the new path.
4. Commit and Vercel will redeploy automatically.

The per-deck `vercel.json` files inside each deck folder are unused by the root deployment; they exist so a single deck folder can also be deployed standalone if needed.

## Project Memory

Review these files before substantial work:

1. `README.md`
2. `MEMORY.md`
3. `doc/PROJECT_STATUS.md`
4. `doc/DECISIONS.md`
5. `doc/BUSINESS_ASSUMPTIONS.md`
6. `doc/WORKLOG.md`

After meaningful work, update the relevant file in `doc/`. After each commit, append one matching record to `doc/DAILY_LOG.md`.

## Directory Layout

| Directory | Purpose |
|-----------|---------|
| `inputs/` | Source notes, interviews, surveys, market exports, and other business-plan inputs |
| `models/` | Financial models, scenario tables, and assumption worksheets |
| `presentations/` | Source HTML-PPT presentation decks, with parallel `investor/` and `internal/` tracks |
| `reports/` | Rendered decks, exported reports, and shareable deliverables |
| `assets/` | Logos, product images, screenshots, charts, and presentation assets |
| `cache/` | Rebuildable intermediate files |
| `doc/` | Project memory, status, assumptions, decisions, and work logs |
| `scripts/` | Small project utilities such as validation and commit logging |

## Core Planning Files

| File | Purpose |
|------|---------|
| `doc/BUSINESS_ASSUMPTIONS.md` | Core assumptions, evidence, confidence, and review status |
| `doc/MARKET_RESEARCH.md` | Market definition, sources, sizing logic, and open gaps |
| `doc/CUSTOMER_DISCOVERY.md` | Interview, survey, and customer validation notes |
| `doc/COMPETITIVE_LANDSCAPE.md` | Competitors, substitutes, differentiation, and risks |
| `doc/FINANCIAL_MODEL_NOTES.md` | Pricing, revenue, cost, margin, growth, and funding assumptions |
| `doc/PITCH_DECK_PLAN.md` | Deck outline, narrative, evidence needs, and review status |
| `doc/PROJECT_STATUS.md` | What is done, active, and next |
| `doc/DECISIONS.md` | Important decisions and why they were made |
| `doc/DAILY_LOG.md` | One human-readable record per commit |
| `doc/WORKLOG.md` | Session notes and handoff context |
| `doc/ENVIRONMENT.md` | Local setup, tools, and reporting workflow notes |

## Template Check

Run this from the repository root after setup or before handoff:

```bash
python3 scripts/doctor.py
```

## License

Free and open source, licensed under [GPLv3](LICENSE). This is a business planning template intended for human-in-the-loop work and adaptation.
