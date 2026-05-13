# Daily Log

## Purpose

Keep one human-readable entry per commit. After each commit, run `python3 scripts/log_commit.py` when available or add one matching entry manually.

Current baseline before the business-plan refactor implementation: `0cf8da6`.

Each entry should include:

- commit hash
- summary of what changed
- main files touched
- result or impact
- next concrete step

## 2026-05-13 - Deck v0.2.1: embed map slide + sources slide in investor deck

- Commit: `eb869e3`
- Summary: Embedded the interactive Leaflet map as a dedicated slide (iframe) inside the investor deck and added a final Sources slide with categorized, clickable links to every public dataset cited (charging stations, traffic, market/policy, apartment cluster).
- Files: `presentations/investor/volt-go-lincoln/index.html`
- Result: Deck is now 13 slides. Map renders inline; sources slide gives investors a one-click trail back to every primary source. Tiles served from OpenStreetMap / CARTO CDN, Leaflet from unpkg CDN — needs network to render the map slide.
- Next concrete step: Owner review and replacement of any DRAFT numbers with verified equivalents before sharing externally.

## 2026-05-13 - Second-pass: candidate site, competitor data, interactive map (v0.2 DRAFT)

- Commit: `1dde39c`
- Summary: Researched real Lincoln-area EV charging competitors and Class A apartment clusters; recommended a candidate site at Fallbrook / Tallgrass (~7300 Tallgrass Pkwy, ~1.5 mi from I-80 Exit 401); built an interactive Leaflet map page plotting the site, all DCFC and selected L2 competitors, Class A apartment clusters, and the I-80 corridor.
- Files: `presentations/investor/volt-go-lincoln/map.html` (new), `presentations/investor/volt-go-lincoln/index.html` (added Site & Competitors slide), `doc/MARKET_RESEARCH.md`, `doc/COMPETITIVE_LANDSCAPE.md`, `doc/DECISIONS.md`, `doc/PROJECT_STATUS.md`
- Result: v0.2 of the deck now includes a 12th slide naming a specific site, drive-time/distance to every competitor, and the only-non-Tesla-DCFC-within-3-miles claim grounded in PlugShare/AFDC/Tesla/EA data. Map opens directly in a browser.
- Key findings: Lincoln has ~155 public ports across ~32 sites but only ~18 DCFC, of which 16 are Tesla. Only 1 open-network DCFC site exists today (Electrify America at Casey's). Nebraska statewide EVs ~9,490 (Jun 2025); Lincoln share ~1,200–1,500 (estimated, unverified).
- Caveats: AADT (30–45k for I-80 through Lincoln) is a planning estimate; apartment unit counts and Lincoln-specific EV count remain DRAFT. Tesla Magic Dock rollout and any NEVI second-round Lincoln award are the two largest competitive risks.
- Next concrete step: Owner pulls one current AFDC API export, drives the Fallbrook site, and gets a parcel availability check + lease quote.

## 2026-05-13 - First investor HTML pitch deck built (v0.1 DRAFT)

- Commit: `2e8cda3`
- Summary: Generated initial 11-slide HTML investor pitch deck for Volt & Go Lincoln using the `html-ppt-skill` `pitch-deck` template. Pulled content from PITCH_DECK_PLAN.md, FINANCIAL_MODEL_NOTES.md, COMPETITIVE_LANDSCAPE.md, and CUSTOMER_DISCOVERY.md.
- Files: `presentations/investor/volt-go-lincoln/index.html`, `presentations/investor/volt-go-lincoln/style.css`
- Result: Browser-renderable deck with speaker notes on every slide. Marked as DRAFT v0.1 in cover footer. Slides flagged for human review: Customers (unvalidated hypotheses), Market (numbers need validation), Business Model (pricing), Financials (land-lease sensitivity), Capital Plan (grants unverified), The Ask (terms TBD).
- Next concrete step: Owner reviews deck content against PITCH_DECK_PLAN.md "Key Slides Requiring Human Review" list before any external use.

## 2026-05-13 - Volt & Go Lincoln EV charging station business plan drafted

- Commit: `2e8cda3` (bundled with deck v0.1)
- Summary: Drafted complete initial business plan for a Lincoln, NE EV charging station with 10 chargers (8 L2 + 2 DCFC), $1M investment, I-80 + high-end apartment dual-positioning.
- Main files touched: `README.md`, `doc/MARKET_RESEARCH.md`, `doc/BUSINESS_ASSUMPTIONS.md`, `doc/FINANCIAL_MODEL_NOTES.md`, `doc/COMPETITIVE_LANDSCAPE.md`, `doc/CUSTOMER_DISCOVERY.md`, `doc/PITCH_DECK_PLAN.md`, `doc/PROJECT_STATUS.md`, `doc/DECISIONS.md`
- Result: Full assumption register, 5-year financial model, competitive analysis, customer hypotheses, and investor deck plan created in draft. Key finding: land lease cost is the primary financial risk; at $4,500/month breakeven requires >5 years; at $3,000/month breakeven is achievable by Y3.
- Next concrete step: Human reviews FINANCIAL_MODEL_NOTES.md and BUSINESS_ASSUMPTIONS.md; identifies target site and gets lease quote from Lincoln commercial broker.


- Files: `doc/DECISIONS.md`, `doc/BUSINESS_PLAN_TEMPLATE_REFACTOR_PLAN.md`, `doc/DAILY_LOG.md`
- Results or impact: The template has a durable record of the business-planning direction, presentation folder choice, dual deck tracks, HTML-PPT assumption, Python utility retention, and deletion strategy.
- Next: Execute the refactor implementation under the canonical Implementation Order in `doc/BUSINESS_PLAN_TEMPLATE_REFACTOR_PLAN.md`.

## 2026-05-13 - implement business plan template refactor

- Commit: `6e2f7e7`
- Summary: Converted the active template structure and documentation to a human-in-the-loop business plan workflow.
- Files: `README.md`, `MEMORY.md`, `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `.gitignore`, `doc/`, `assets/`, `inputs/`, `models/`, `presentations/`, `scripts/doctor.py`
- Results or impact: The repository now uses business-plan memory files, presentation-oriented reporting, parallel investor/internal deck folders with slide-by-slide starter sources, and business-template validation checks. `python3 scripts/doctor.py` passes 0 failures, 0 warnings.
- Next: Start the first real business plan project by filling README metadata and the six business-plan memory docs, then author the investor and internal decks using the `html-ppt-skill`.
