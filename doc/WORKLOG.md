# Work Log

## Purpose

Keep short dated notes so a business planner or AI assistant can resume work quickly.

## 2026-05-13

- Linked the repository remote to `git@github.com:yangjl/busplan.git`.
- Drafted `doc/BUSINESS_PLAN_TEMPLATE_REFACTOR_PLAN.md` to guide the conversion into a human-in-the-loop business plan template.
- Recorded the business-template decisions in `doc/DECISIONS.md`, including source presentations in `presentations/`, parallel investor/internal deck tracks, Python utility retention, and the HTML-PPT skill prerequisite.
- Added business-plan folders and memory docs for assumptions, market research, customer discovery, competitive landscape, financial model notes, and pitch deck planning.
- Rewrote README, MEMORY, assistant instructions, environment notes, checklist, status, ignore rules, and validation checks for the business-plan workflow.
- Removed the old research-analysis and local web-dashboard scaffold from the active template structure.
- Ran `python3 scripts/doctor.py`; validation passed with zero failures and zero warnings.
- Reviewed the Volt & Go Lincoln EV charging station plan and created `reports/revised_ev_charging_station_business_plan_report.md`.
- Key revision from the report: treat the concept as a site-validation and incentive-eligibility plan, not a ready-to-fund plan. Owner must decide whether to keep the 8 L2 + 2 DCFC mixed-use design or redesign around 4+ DCFC ports for stronger corridor/NEVI fit.
- Improved the investor HTML deck with a candidate Volt&Go wordmark, removed seed-investment language, added formula-backed demand sizing, clarified NEVI/Section 30C requirements, added Fallbrook site-selection rationale, added membership-projection math, and expanded the map with highway labels plus a draft peak-hour traffic heat overlay.

## 2026-05-14

- Pulled latest GitHub changes (`ac97a51`) into the local workspace.
- Created a South Lincoln alternative research scenario in `reports/south_lincoln_location_optimization_report.md`.
- Added `models/south_lincoln_optimization_summary.csv` comparing stall mixes and five-year modeled economics.
- Draft conclusion: SouthPointe / Pine Lake / S 27th is the strongest South Lincoln candidate zone. The operating-profit-maximizing mix is 16 L2 + 2 DCFC, with ~$808K gross capex, ~$237K five-year cumulative EBITDA, and ~$107K Year 5 EBITDA. No tested configuration recovers full capex inside five years under base assumptions.
- Fixed South Lincoln report review issues: added annual EBITDA, sensitivity analysis, maintenance assumptions, cautious DCFC-gap language, and Section 30C deadline treatment.
- Started a separate South Lincoln HTML diligence deck at `presentations/investor/volt-go-south-lincoln/index.html`, reusing the current Volt&Go visual style but focused on SouthPointe / Pine Lake / S 27th.
- Added South Lincoln deck data depth and map context: demand-stack slide, embedded candidate-zone map, road labels, traffic-context heat overlays, nearby charging context, and `/map` Vercel route.
- Revised the South Lincoln deck per owner feedback: removed the separate charging-gap slide after owner confirmation of no regional DCFC, added North 27th Tesla Supercharger context, adjusted US-77 / Nebraska Parkway / Hwy 2 map lines, and changed the deck recommendation to 16 L2 + 3 DCFC with a comparison graph.
- Created a third fixed owner-lot scenario at 84th & Nebraska Parkway near Sam's Club. Added `reports/84th_nebraska_parkway_fixed_site_analysis.md`, `models/84th_nebraska_pkwy_optimization_summary.csv`, `models/84th_nebraska_pkwy_recommended_build_annual_ebitda.csv`, and `models/84th_nebraska_pkwy_site_comparison.csv`. Draft result: 20 L2 + 4 DCFC maximizes five-year operating EBITDA; 12 L2 + 4 DCFC is the lower-risk phase-one fallback.
- Added a separate owner-lot deck at `presentations/investor/volt-go-84th-nebraska-pkwy/` with `index.html`, `map.html`, Vercel routing, and copied HTML-PPT runtime/theme assets from the South Lincoln deck.
- Recalculated and clarified the 84th deck headline metrics: exact derisk-launch 5-year cumulative EBITDA is $903,565, displayed as $904K; five-year cash after capex is ($30,435), displayed as ($30K). Updated cover/front slide, build ladder, comparison, map sidebar, report summary, and supporting CSVs to keep EBITDA separate from after-capex cash.

## 2026-06-13

- Reviewed and revised the I-80 corridor analysis deck in both source locations: `presentations/internal/us80-corridor/index.html` and deployed copy `presentations/investor/volt-go-lincoln/corridor/index.html`.
- Kept the existing green highway HTML-PPT style, but softened overconfident investment language: the score is now a diligence-priority screen, not a forecast or capital recommendation.
- Revised the recommendation from "four top-ranked sites" to "Rock Springs + Elko first; Lincoln remains the mixed-model benchmark; Iowa City and Evanston are watchlist unless partner/grant timing improves."
- Corrected the capital-stack story by excluding §30C from the I-80 corridor base case because the placed-in-service deadline is June 30, 2026.
- Updated the landing page card, `doc/PROJECT_STATUS.md`, `doc/DECISIONS.md`, `doc/BUSINESS_ASSUMPTIONS.md`, and `doc/MARKET_RESEARCH.md` so future review sees the same corridor interpretation.
