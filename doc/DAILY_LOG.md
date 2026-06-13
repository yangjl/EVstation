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

## 2026-06-13 - v0.5: I-80 corridor systematic site analysis + mobile fix + dashboard link

- Commit: pending
- Summary: Built a full 14-slide HTML-PPT corridor analysis (`presentations/internal/us80-corridor/index.html`) and deployed copy (`presentations/investor/volt-go-lincoln/corridor/index.html`). Green highway theme. Defines a 5-factor scoring model (traffic, DCFC gap, EV density, amenity anchor, grant eligibility) and scores 8 I-80 sites. Top-ranked: Rock Springs WY and Elko NV (both 18/25); Lincoln NE / Volt&Go (17/25) and Iowa City IA (17/25) as mixed-model anchors. Fixed mobile overflow on corridor deck (`overflow-x:hidden !important; overflow-y:auto !important` to beat base.css shorthand; `.table-scroll` wrappers for state table and score grid). Added `/corridor` Vercel rewrite and "I-80 Corridor Site Analysis →" link on the investor deck cover.
- Files: `presentations/internal/us80-corridor/index.html`, `presentations/internal/us80-corridor/style.css`, `presentations/investor/volt-go-lincoln/corridor/index.html`, `presentations/investor/volt-go-lincoln/corridor/style.css`, `presentations/investor/volt-go-lincoln/vercel.json`, `presentations/investor/volt-go-lincoln/index.html`, `reports/us80-corridor-ev-analysis.html`, `doc/PROJECT_STATUS.md`
- Result: Lincoln confirmed as #3 corridor site — compensates lower DCFC gap score with higher local EV density and amenity anchor; the only site with a viable membership revenue model. Corridor deck accessible at /corridor from investor deck Vercel deployment.
- Next concrete step: Human review of corridor scores and decision on whether to pursue Rock Springs or Elko diligence in parallel with Lincoln.

## 2026-05-14 - Mobile nav on all 3 decks + Fallbrook financials slide fix + landing rounding

- Commit: `5dcbe11`
- Summary: (1) Ported the Fallbrook deck's mobile swipe handler and bottom prev/next nav-bar to the SouthPointe and 84th decks — they had the CSS but were missing the JS shim. Now all three decks advance on mobile via horizontal swipe or via the bottom buttons. (2) Rebuilt Fallbrook slide 7 (Financials) — it was showing revenue bars labeled with positive numbers ($63K → $171K) while the landing page card correctly showed −$206K cumulative EBITDA, which read as a contradiction. New slide shows revenue (gradient) + OpEx (gray) as paired bars per year with the EBITDA gap called out in red underneath, plus an explicit note that the $4,500/mo land lease ($54K/yr) keeps OpEx above revenue every year. (3) Reconciled landing-page card rounding: Fallbrook −$205K → −$206K; 84th derisk +$903K → +$904K, matching CSV values $206,150 and $903,565.
- Files: `presentations/investor/volt-go-lincoln/index.html` (financials slide + mobile nav), `presentations/investor/volt-go-south-lincoln/index.html` (mobile nav added), `presentations/investor/volt-go-84th-nebraska-pkwy/index.html` (mobile nav added), `index.html` (landing rounding). Owner intervening edits also captured: deck cover data-strip added to 84th, refined annual EBITDA CSV (Y1 $25k → $28,472; cum $903,565), map sidebar metrics updated to derisk numbers, DECISIONS.md and WORKLOG.md entries for the 84th deck creation.
- Result: All three deck URLs are now mobile-usable. Fallbrook financials slide is no longer misleading. Every landing-card number reconciles to the source CSV.
- Next concrete step: Owner picks the SouthPointe and 84th deck Annual EBITDA slides — should they get the same paired revenue+OpEx visual the Fallbrook slide now has? (Existing EBITDA-only bars on those two are accurate but less explicit about *why* EBITDA is shaped the way it is.)

## 2026-05-14 - 84th & Nebraska Pkwy deck derisk pivot (v0.4 → 8 L2 + 4 DCFC)

- Commit: `042573f`
- Summary: Rebuilt the 84th & Nebraska Pkwy investor/diligence deck around an **8 L2 + 4 DCFC derisk launch** at ~$934K capex (was 20 L2 + 4 DCFC at $1.15M). The four DCFC stalls — which drive ~80% of operating margin — are preserved; L2 count is dialed down for capital protection, with conduit/switchgear engineered for later expansion to 20 L2. Net result: $216K less capex, only $49K less Y5 EBITDA, and 5-yr cash gap shrinks from ($104K) to ($31K).
- Deck rebuilt at 16 slides with deeper data: Demand Math (bottom-up Y5 derivation: ~$208K DCFC + ~$67K L2 + ~$9K membership − ~$70K energy − ~$52K fixed OpEx − ~$32K maintenance = ~$305K Y5), Direct Competitors (in-trade-area L2 and 9-mi-away DCFC), Build Ladder (0+4 / 4+4 / 8+4 highlighted / 12+4 / 20+4 ceiling), Capital Recovery (Y1-Y6 cumulative cash), Sensitivity (4 cases from $185K downside to $345K upside), and a like-for-like 3-Site Comparison showing the derisk pick wins on capex, Y5 EBITDA, 5-yr cum, and payback simultaneously.
- New CSVs: `models/84th_nebraska_pkwy_derisk_8L2_4DCFC_annual_ebitda.csv` (Y1-Y8 ramp + cumulative cash), `models/three_site_comparison_v2.csv` (build-for-build comparison adding the derisk row alongside the full-build ceiling row).
- Report updated: `reports/84th_nebraska_parkway_fixed_site_analysis.md` executive summary now leads with the derisk recommendation and includes a build-for-build comparison table. The 20 L2 + 4 DCFC ceiling is preserved as the long-term operating-profit target, committed to only after Y2-Y3 utilization validates.
- Map updated: planning-metrics sidebar and candidate-site popup now show 8 + 4 derisk figures, not 20 + 4 full-build figures.
- Landing page updated: replaced the East Lincoln placeholder card with a fully populated 84th card; updated lede to "Three site scenarios" and summary strip count from 2 → 3.
- Files: `presentations/investor/volt-go-84th-nebraska-pkwy/index.html`, `presentations/investor/volt-go-84th-nebraska-pkwy/map.html`, `reports/84th_nebraska_parkway_fixed_site_analysis.md`, `index.html`, `models/84th_nebraska_pkwy_derisk_8L2_4DCFC_annual_ebitda.csv` (new), `models/three_site_comparison_v2.csv` (new), plus owner-authored `presentations/investor/volt-go-84th-nebraska-pkwy/README.md` and `vercel.json`.
- Next concrete step: Owner pulls the AFDC API export for a 10-mi radius around 84th & Nebraska Pkwy, requests LES written demand-charge quote for 4 × 100 kW + 8 × 7.2 kW load, and starts the civil/turning review.

## 2026-05-14 - Root-level Vercel landing page for site scenarios

- Commit: `9f4ac3d`
- Summary: Added a top-level `index.html` landing page that lists every site-scenario deck as a card, and a root `vercel.json` that rewrites clean URLs (`/north`, `/north/map`, `/south`, `/south/map`) onto the per-deck folders. Both active scenarios (Fallbrook v0.2 and SouthPointe v0.3.1) get fully-populated cards with build/capex/5y-EBITDA/I-80-access stats; three `.placeholder` cards sit below ready to be filled when the owner picks the next site (suggested: East 84th/O, West Haymarket/Pioneers, plus one open slot).
- Files: `index.html` (new), `vercel.json` (new), `README.md` (added Hosted Landing Page section with Vercel project settings + "Adding a new site scenario" four-step recipe)
- Result: Owner can deploy the repo root to Vercel with default settings. Browser shows landing at `/` with two scenario cards and three placeholders. Per-deck Vercel configs under each presentation folder are unaffected — they remain valid for standalone subfolder deployments.
- Next concrete step: Owner connects a Vercel project to the repo root (or moves the existing deck Vercel projects under a single root project), verifies `/north` and `/south` load the right decks, and decides which placeholder card to fill next.

## 2026-05-14 - South Lincoln deck v0.3.1: data audit + 3 new evidence slides

- Commit: `8e16925`
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
