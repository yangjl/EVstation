# Project Status

## Purpose

Check here first to understand where the business plan stands. This file tracks what has been done, what is active, and what should happen next.

## Current Project: Volt & Go Lincoln — EV Charging Station

**As of:** 2026-05-14 (v0.3 research scenario)
**Phase:** Initial planning — Fallbrook v0.2 plus South Lincoln alternative scenario; awaiting human review

## Completed

- Established shared instruction files for Codex, Claude Code, and GitHub Copilot (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`).
- Set up repository-native tracking files for status, decisions, environment notes, work logs, and daily commit journal.
- Drafted full initial business plan for Volt & Go Lincoln EV charging station including:
  - `README.md` — updated with project identity, business snapshot, and metadata
  - `doc/MARKET_RESEARCH.md` — Lincoln NE EV market context, evidence log, market sizing draft, open questions
  - `doc/BUSINESS_ASSUMPTIONS.md` — full assumption register covering capital, operations, revenue, and funding
  - `doc/FINANCIAL_MODEL_NOTES.md` — 5-year revenue/cost model, capital stack, sensitivity analysis, scenario table
  - `doc/COMPETITIVE_LANDSCAPE.md` — competitor register (Electrify America, ChargePoint, Tesla, Blink, home charging) and differentiation strategy
  - `doc/CUSTOMER_DISCOVERY.md` — three customer segment hypotheses; discovery priorities flagged for human action
  - `doc/PITCH_DECK_PLAN.md` — 13-slide investor deck outline with evidence needs and go-to-market detail
- Created `reports/revised_ev_charging_station_business_plan_report.md`, a revised owner-review report that reframes the plan around site validation, NEVI/design fit, utility-rate diligence, and customer discovery.
- **v0.2 (2026-05-13):** Pulled real Lincoln-area competitor data (PlugShare, ChargeHub, AFDC, Tesla/EA locators), identified Fallbrook/Tallgrass candidate site, built `presentations/investor/volt-go-lincoln/map.html` (interactive Leaflet map of site + competitors + apartments + I-80 exits), updated `MARKET_RESEARCH.md` and `COMPETITIVE_LANDSCAPE.md` with real numbers, added a Site & Competitors slide to the investor deck, recorded site recommendation in `DECISIONS.md`.
- **v0.3 research scenario (2026-05-14):** Created `reports/south_lincoln_location_optimization_report.md` and `models/south_lincoln_optimization_summary.csv` comparing South Lincoln stall mixes. Draft conclusion: SouthPointe / Pine Lake / S 27th is the strongest South Lincoln candidate zone; 16 L2 + 2 DCFC maximizes modeled five-year operating EBITDA, but no tested build recovers full capex inside five years under base assumptions.
- **v0.3 audit (2026-05-14):** Built `presentations/investor/volt-go-lincoln/south_lincoln_map.html` (Leaflet map: SouthPointe candidate, ChargePoint competitor, Aventine / Level apartments, Pine Lake / S 27th / Hwy 2 / US-77 with AADT). Appended §11 audit/improvement memo to `reports/south_lincoln_location_optimization_report.md` covering: math sanity check (Y5 EBITDA back-of-envelope = ~$151k vs report's $107k, gap explained), operating breakeven Y1-Y2 (sooner than executive summary implies), capex recovery curve at Y8-Y10 (reframe of "do not proceed"), Section 30C unavailable (47 days to deadline → effectively zero), two assumptions worth challenging (DCFC saturation cap; 32% mature L2 utilization), north-vs-south comparison table on a single set of axes. Fixed DECISIONS.md (removed Brookside/Northbrook leftover from south Lincoln entry; added §30C-unavailable decision).

## In Progress

- Awaiting human review of all draft assumptions, especially:
  1. Land lease cost/structure (highest model sensitivity)
  2. NEVI/IRA grant eligibility confirmation with Nebraska DOT
  3. Customer discovery fieldwork (apartment residents, property managers, EV drivers)
  4. Choice between the current 8 L2 + 2 DCFC mixed-use design and a 4+ DCFC corridor-oriented design.
  5. Whether South Lincoln should supersede Fallbrook as the active site strategy.

## Next Steps (Prioritized)

1. **Human review:** Owner reviews `FINANCIAL_MODEL_NOTES.md` and confirms investment parameters, land cost targets, and pricing
2. **Site selection:** Identify 2–3 candidate parcels near I-80 interchanges adjacent to Class A apartment clusters in Lincoln; get lease/purchase quotes
3. **Utility quote:** Contact Lincoln Electric System (LES) for a commercial rate quote under the station's DCFC load profile — demand charges are critical
4. **Grant research:** Contact Nebraska DOT NEVI program office and Nebraska Energy Office for application timelines and eligibility
5. **Customer discovery:** Survey 20–30 apartment EV owners in target area; interview 3–5 property managers
6. **Equipment quotes:** Solicit charger hardware quotes (ChargePoint, ABB, BTC Power) and installation contractor bids
7. **Build pitch deck:** Once key assumptions are human-reviewed, build HTML-PPT investor deck per `doc/PITCH_DECK_PLAN.md`
8. **South Lincoln validation:** If owner prefers South Lincoln, contact SouthPointe/RED Development and LES, then validate the 16 L2 + 2 DCFC operating model before revising the live investor deck.

## Open Questions — Require Human Decision

1. **Site:** Is the owner targeting a specific I-80 exit or neighborhood? (Wilderness Hills, Fallbrook, South 27th area, etc.)
2. **Business name:** Is "Volt & Go Lincoln" the intended brand, or placeholder only?
3. **Ownership structure:** Sole proprietor, LLC, or partnership? Matters for SBA loan and investor terms.
4. **Land strategy:** Buy vs. lease vs. partnership with apartment developer or city?
5. **Network platform:** Will the station use ChargePoint, EV Connect, or build independent network management?
6. **The Ask:** What are the exact investor terms, expected return, and timeline to exit or refinance?
