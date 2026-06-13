# Project Status

## Purpose

Check here first to understand where the business plan stands. This file tracks what has been done, what is active, and what should happen next.

## Current Project: Volt & Go Lincoln — EV Charging Station

**As of:** 2026-06-13 (v0.5.1)
**Phase:** Three candidate sites modeled (Fallbrook, South Lincoln, 84th/Nebraska Pkwy); I-80 corridor analysis added; all awaiting human review

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
- **v0.2 (2026-05-13):** Pulled real Lincoln-area competitor data (PlugShare, ChargeHub, AFDC, Tesla/EA locators), identified Fallbrook/Tallgrass candidate site, built `presentations/investor/volt-go-lincoln/map.html`, updated `MARKET_RESEARCH.md` and `COMPETITIVE_LANDSCAPE.md` with real numbers, added Site & Competitors slide to investor deck, recorded site recommendation in `DECISIONS.md`.
- **v0.3 research scenario (2026-05-14):** Created `reports/south_lincoln_location_optimization_report.md` and `models/south_lincoln_optimization_summary.csv` comparing South Lincoln stall mixes. Draft conclusion: SouthPointe / Pine Lake / S 27th is the strongest South Lincoln candidate zone; 16 L2 + 2 DCFC maximizes modeled five-year operating EBITDA, but no tested build recovers full capex inside five years under base assumptions.
- **v0.3 deck start (2026-05-14):** Started a separate South Lincoln diligence deck at `presentations/investor/volt-go-south-lincoln/index.html` with the same visual system as the North/Fallbrook deck. Added annual EBITDA and sensitivity CSVs, plus a demand-stack slide and embedded South Lincoln planning map. Owner feedback revised the deck recommendation from 16 L2 + 2 DCFC to 16 L2 + 3 DCFC after confirming no DCFC around the South Lincoln region.
- **v0.3 audit (2026-05-14):** Built `presentations/investor/volt-go-lincoln/south_lincoln_map.html`. Appended §11 audit/improvement memo to `reports/south_lincoln_location_optimization_report.md`. Fixed DECISIONS.md.
- **v0.4 fixed owner-lot scenario (2026-05-14):** Created `reports/84th_nebraska_parkway_fixed_site_analysis.md` and model CSVs for the owner-controlled lot near Sam's Club at 84th / Nebraska Parkway. Draft model recommends 8 L2 + 4 DCFC derisk launch with ~$904K five-year cumulative EBITDA.
- **v0.4 deck (2026-05-14):** Added separate HTML-PPT deck at `presentations/investor/volt-go-84th-nebraska-pkwy/index.html` with embedded planning map, optimization graph, phase strategy, annual EBITDA, three-site comparison, and risk/diligence slides.
- **v0.5 corridor analysis (2026-06-13):** Built full I-80 corridor systematic analysis (`presentations/internal/us80-corridor/index.html`, deployed as `presentations/investor/volt-go-lincoln/corridor/index.html`). 14-slide HTML-PPT deck scores 8 sites across 5 criteria (traffic, DCFC gap, EV density, amenity anchor, grant eligibility). Top scored sites: Rock Springs WY (18/25), Elko NV (18/25), Lincoln NE / Volt&Go (17/25), Iowa City IA (17/25). Fixed mobile overflow on the corridor deck. Added `/corridor` Vercel route and "I-80 Corridor Site Analysis →" link on the investor deck cover.
- **v0.5.1 corridor revision (2026-06-13):** Revised the I-80 analysis narrative and deployed/internal decks while preserving the green highway visual style. The deck now treats scores as diligence priority, not investability; moves Rock Springs + Elko forward as the two immediate corridor-gap checks; keeps Lincoln as the mixed-model benchmark; moves Iowa City/Evanston to watchlist; and removes §30C from base-case corridor capital planning because the June 30, 2026 placed-in-service deadline is too near for new sites.

## In Progress

- Awaiting human review of all draft assumptions, especially:
  1. Land lease cost/structure (highest model sensitivity)
  2. NEVI/IRA grant eligibility confirmation with Nebraska DOT
  3. Customer discovery fieldwork (apartment residents, property managers, EV drivers)
  4. Choice between the current 8 L2 + 2 DCFC mixed-use design and a 4+ DCFC corridor-oriented design.
  5. Whether the 84th / Nebraska Parkway owner-lot scenario should supersede Fallbrook and South Lincoln as the active site strategy.
- Corridor analysis complete but all scores and the revised Rock Springs + Elko prioritization are preliminary estimates — human review required before using to direct capital.

## Next Steps (Prioritized)

1. **Human review:** Owner reviews `FINANCIAL_MODEL_NOTES.md` and confirms investment parameters, land cost targets, and pricing.
2. **Site selection decision:** Choose between Fallbrook, South Lincoln, and 84th/Nebraska Pkwy as the active site; get lease/purchase quotes.
3. **Utility quote:** Contact Lincoln Electric System (LES) for a commercial rate quote under the station's DCFC load profile — demand charges are critical.
4. **Grant research:** Contact NE DOT NEVI, WY DOT NEVI (Round 2), NV DOT NEVI, IA DOT NEVI for application timelines and eligibility per site.
5. **Customer discovery:** Survey 20–30 apartment EV owners in target area; interview 3–5 property managers.
6. **Equipment quotes:** Solicit charger hardware quotes (ChargePoint, ABB, BTC Power) and installation contractor bids.
7. **South Lincoln validation:** If owner prefers South Lincoln, contact SouthPointe/RED Development and LES, verify map pins/traffic counts with source exports, then validate the revised 16 L2 + 3 DCFC operating model.
8. **84th / Nebraska Parkway validation:** If owner prefers the fixed lot, order LES load quote, civil/turning review, and parking/covenant check for the 8 L2 + 4 DCFC derisk launch.
9. **Corridor expansion (optional):** If owner decides to pursue Rock Springs or Elko, initiate parcel inquiry, utility demand-charge request, and NEVI pre-application contact with WYDOT / Nevada DOT.

## Open Questions — Require Human Decision

1. **Site:** Is the owner targeting Fallbrook, South Lincoln, or 84th/Nebraska Pkwy as the primary candidate?
2. **Business name:** Is "Volt & Go Lincoln" the intended brand, or placeholder only?
3. **Ownership structure:** Sole proprietor, LLC, or partnership? Matters for SBA loan and investor terms.
4. **Land strategy:** Buy vs. lease vs. partnership with apartment developer or city?
5. **Network platform:** Will the station use ChargePoint, EV Connect, or build independent network management?
6. **The Ask:** What are the exact investor terms, expected return, and timeline to exit or refinance?
