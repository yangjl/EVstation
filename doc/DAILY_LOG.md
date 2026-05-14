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

## 2026-05-14 - South Lincoln deck v0.3.1: data audit + 3 new evidence slides

- Commit: (pending)
- Summary: Audited the revised South Lincoln deck (`presentations/investor/volt-go-south-lincoln/index.html`) and found three sync/data issues plus three missing evidence sections. Fixed the inconsistencies and added the new slides.
- Issues found: (1) the Annual EBITDA slide showed 3-DCFC numbers ($164k Y5, $433k cum) but the supporting CSV in `models/` was still the 2-DCFC build; (2) the Sensitivity slide's "$50k downside" had no CSV behind it; (3) the §30C slide hedged ("research indicates") despite the deadline being firm at 2026-06-30 (47 days away).
- New CSVs: `models/south_lincoln_revised_3dcfc_annual_ebitda.csv` (Y1-Y10 with cumulative cash by year — for the capital-recovery slide), `models/south_lincoln_revised_3dcfc_sensitivity.csv` (7-row matrix across 24%/32%/40% L2 utilization × 1.6/2.2/3.0 DCFC saturation).
- New slides (deck now 16, was 13):
  - **02a · Demand math** — bottom-up Y5 EBITDA derivation: 25,430 ADT × 1% EV share → 250 EVs/day pass site → ~20 fast-charge sessions/day across 3 DCFC stalls = ~$108k DCFC; 1,500 Lincoln EVs × 15% catchment × 30% no-home-charging × 60% conversion = ~40 paying members; 16 L2 × 32% util × $0.38/kWh = ~$123k L2; sums to ~$164k Y5.
  - **03b · Direct competitors** — in-zone ChargePoint L2 at 2980 Pine Lake ($1.50/hr undercuts our $0.38/kWh, edge must be reservations + canopy + apartment pass); out-of-zone DCFC table showing all 20 of Lincoln's existing DCFC ports are 7-10 mi N/NW.
  - **05b · Capital recovery** — Y1-Y9 cumulative cash bar chart showing the project pays back ~$953k capex around Year 8-9 under base assumptions (turns operating-positive in Y2). Reframes the "5-yr cash = -$520k" line that has been misread as "do not proceed."
- Tightened existing slides:
  - Sensitivity now a 4-card matrix (downside / conservative / base / upside) traceable to the new CSV
  - North-vs-South now shows a build-for-build comparable table with the $638k 5-yr EBITDA delta dollar figure and the cost-structure driver call-out
  - §30C slide rewritten to be definitive: $0 credit in capital plan; counterfactual quantified ($210k credit forfeit); 4 substitute paths listed
- Files: `presentations/investor/volt-go-south-lincoln/index.html`, `models/south_lincoln_revised_3dcfc_annual_ebitda.csv` (new), `models/south_lincoln_revised_3dcfc_sensitivity.csv` (new), `doc/DAILY_LOG.md`
- Result: Deck v0.3.1 has 16 slides; every dollar figure on the deck now traces to a CSV in `models/` or the audit memo in `reports/south_lincoln_location_optimization_report.md` §11.
- Next concrete step: Owner reviews the new Demand-math and Capital-recovery slides for narrative fit before any external use; then validates the three biggest demand-math inputs (1% EV share of passing traffic, 30% no-home-charging, 60% member conversion) through field discovery.

## 2026-05-14 - South Lincoln scenario audit + map (v0.3 research)

- Commit: `035998a`
- Summary: Audited the south Lincoln optimization report and stall-mix CSV (16 L2 + 2 DCFC, $808k capex, $237k five-year cum EBITDA). Verified the internal math, called out an unstated operating-cashflow-positive Y1-Y2 result, flagged that capex recovery is realistic at Y8-Y10 rather than impossible, removed §30C from any forward capital plan because of the 2026-06-30 placed-in-service deadline (47 days away), and noted two aggressive assumptions worth challenging (DCFC saturation cap of 2.2 stalls; 32% mature L2 utilization). Built a south-Lincoln Leaflet map plotting the SouthPointe candidate, ChargePoint competitor at 2980 Pine Lake Rd, Aventine and Level apartments, the Pine Lake / S 27th / Hwy 2 / US-77 arterials with AADT, and a small distant indicator showing I-80 is ~7 mi north. Added a north-vs-south comparison table to the report; the headline insight is that cost structure (retail-host vs standalone lease) is the real driver of the $442k five-year EBITDA delta, not geography per se.
- Files: `presentations/investor/volt-go-lincoln/south_lincoln_map.html` (new), `reports/south_lincoln_location_optimization_report.md` (added §11 audit), `doc/DECISIONS.md` (fixed Brookside/Northbrook leftover in south Lincoln entry; added §30C-unavailable decision), `doc/PROJECT_STATUS.md` (recorded v0.3 audit), `doc/DAILY_LOG.md`
- Result: South Lincoln scenario remains a research alternative — the active investor deck stays on Fallbrook v0.2 per project memory rules. The owner now has a defensible comparison memo and a south-Lincoln map for in-person diligence.
- Next concrete step: Owner decides whether to (a) contact RED Development at SouthPointe re: a host-pad, (b) re-run the optimization at DCFC saturation = 1.6/2.2/3.0 and L2 mature utilization = 24%/32%, or (c) keep Fallbrook v0.2 and abandon south Lincoln.

## 2026-05-13 - Deck v0.2.2: mobile-compatible investor deck

- Commit: pending
- Summary: Made the Volt&Go Lincoln investor deck usable on phones. Added a `@media (max-width:820px)` breakpoint that lets each slide scroll vertically inside the fixed-viewport frame, collapses the g2/g3/g4 grids and the data-strip / funnel layouts to single column, shrinks display typography (h1 86→34px, h2 62→26px, metric .n 72→44px), repositions the cover wordmark and footer, and re-anchors the map-slide captions. Added a touch-swipe handler that dispatches synthetic `ArrowLeft`/`ArrowRight` keydown events so the existing keyboard nav, animations, and progress wiring stay single-sourced. Added a small bottom-of-screen prev/next button bar with a page indicator that mirrors the deck's own counter via MutationObserver. Inline overrides in `index.html` shadow `style.css` for `.map-caption` and `.src-grid` so the cascade resolves correctly on mobile.
- Files: `presentations/investor/volt-go-lincoln/style.css`, `presentations/investor/volt-go-lincoln/index.html`
- Result: Deck content reflows cleanly down to ~360px viewports. Map slide skips swipe to keep pan/zoom usable; all other slides advance on horizontal swipe or tap. Desktop layout unchanged.
- Next concrete step: Manually test on a real iPhone/Android device, then have the owner verify the financial bar chart and sources slide remain readable before sharing the link externally.

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

## 2026-05-13 - make investor deck deployable on Vercel

- Commit: `e0bf880`
- Summary: Made the Volt & Go Lincoln investor HTML deck self-contained for Vercel by replacing local HTML-PPT asset paths with vendored relative assets and adding explicit Vercel static routing.
- Files: `presentations/investor/volt-go-lincoln/README.md`, `presentations/investor/volt-go-lincoln/index.html`, `presentations/investor/volt-go-lincoln/vendor/html-ppt/animations/animations.css`, `presentations/investor/volt-go-lincoln/vendor/html-ppt/base.css`, `presentations/investor/volt-go-lincoln/vendor/html-ppt/fonts.css`, `presentations/investor/volt-go-lincoln/vendor/html-ppt/runtime.js`, `presentations/investor/volt-go-lincoln/vercel.json`
- Results or impact: The full deck can now be deployed from presentations/investor/volt-go-lincoln as a static Vercel site, with / serving index.html and /map serving the standalone map.
- Next: Redeploy the Vercel project from the latest main branch and verify the bare deployment URL shows the full deck.

## 2026-05-13 - improve investor deck evidence and site story

- Commit: `d10b964`
- Summary: Improved the Volt & Go Lincoln investor deck with a candidate wordmark, diligence-not-seed framing, formula-backed market/customer estimates, NEVI and Section 30C requirement notes, Fallbrook site rationale, membership math, and map traffic/highway overlays.
- Files: `doc/WORKLOG.md`, `presentations/investor/volt-go-lincoln/index.html`, `presentations/investor/volt-go-lincoln/map.html`, `presentations/investor/volt-go-lincoln/style.css`
- Results or impact: The deck now better supports its conclusions with visible assumptions and source notes while keeping the Fallbrook recommendation in human-review/diligence status.
- Next: Redeploy Vercel from main and review the live deck for slide fit, map rendering, and source wording before external sharing.
