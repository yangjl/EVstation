# Business Assumptions — Volt & Go Lincoln EV Charging Station

## Purpose

Track the core assumptions behind the business plan, the evidence supporting them, and the current review status.

> **All assumptions below are in DRAFT status. Human review is required before using in investor materials, funding applications, or public presentations.**

## Assumption Register

| Assumption | Area | Evidence | Confidence | Review status | Next check |
|------------|------|----------|------------|---------------|------------|
| Total project investment is ~$1,000,000 | cost | Owner-specified. Breakdown modeled in FINANCIAL_MODEL_NOTES.md. | high (as a constraint) | draft | Validate against contractor quotes and equipment bids |
| Station hosts 10 chargers: 8 Level 2 (L2) + 2 DC Fast Chargers (DCFC) | operations | Owner-specified configuration. Industry-standard mix for dual-use highway/residential station. | high (as a constraint) | draft | Confirm charger models and specs; L2 at 7.2kW, DCFC at 50–150kW |
| Site is near I-80 and high-end apartments in Lincoln, NE | location | Owner-specified. Confirmed conceptually via Lincoln urban geography and apartment cluster data. | high (as a constraint) | draft | Identify specific parcel; verify zoning, setbacks, utility access |
| Monthly land lease cost: $4,000–$5,500/month | cost | Estimated from Lincoln commercial land lease comparables near I-80 corridors | medium | draft | Get actual lease quote from property owner or broker |
| Lincoln Electric System commercial rate: $0.09–0.11/kWh | cost | LES published commercial rate schedules; demand charge component may be significant | medium | draft | Get firm LES rate quote for the specific load profile (particularly demand charges) |
| Level 2 charging price: $0.38/kWh | pricing | Mid-range of comparable mid-size market operators (ChargePoint, EVgo, local) | medium | draft | Benchmark against existing Lincoln/Omaha charging prices |
| DCFC charging price: $0.49/kWh | pricing | Mid-range of comparable DCFC operators in the Midwest | medium | draft | Benchmark against existing Lincoln/Omaha DCFC prices |
| Avg L2 session delivers 8 kWh | operations | Industry average for ~60-min Level 2 session at 7.2kW | medium | draft | Validate against ChargePoint/Blink session data |
| Avg DCFC session delivers 30 kWh | operations | Industry average for ~25–35 min DCFC session at 50–150kW | medium | draft | Validate against DCFC network operator data |
| L2 charger utilization ramp: 12% Y1 → 20% Y2 → 28% Y3+ | demand | Conservative ramp based on market-entry benchmarks for new stations | low | draft | Human review required — highly sensitive to local demand |
| DCFC utilization ramp: 18% Y1 → 28% Y2 → 38% Y3+ | demand | Higher initial utilization from highway travelers; benchmarked against comparable I-80 stops | low | draft | Human review required — highly sensitive to highway traffic volumes |
| NEVI or state grant funding: $100,000–$200,000 | funding | Nebraska participates in NEVI formula program; grants cover up to 80% of eligible charger costs | medium | draft | Confirm eligibility, application timeline, and matching requirements with Nebraska DOT |
| Charger hardware cost: L2 ~$7,000–$10,000/unit; DCFC ~$40,000–$80,000/unit | cost | Published equipment pricing from ChargePoint, ABB, BTC Power, EV Connect | medium | draft | Solicit actual equipment quotes |
| Electrical infrastructure/utility interconnect: $150,000–$200,000 | cost | Estimated for commercial transformer upgrade and trenching; highly site-dependent | low | draft | Get electrical engineering site assessment |
| Maintenance cost: ~$20,000–$30,000/year | cost | Industry benchmark ~$1,500–$3,000/charger/year blended across L2 and DCFC | medium | draft | Confirm with service contract quotes |
| Annual revenue growth: 20% Y2, 15% Y3, 10% Y4–5 | growth | Assumes EV adoption growth + maturation of utilization rates | low | draft | Human review required — sensitive to local EV growth trajectory |
| Breakeven at station level (before debt service): Year 3 | financial | Modeled from utilization ramp and cost structure below | low | draft | Human review required before sharing with investors |
| 84th & Nebraska Parkway owner-lot scenario uses owned-land economics | location / cost | Owner provided fixed lot near Sam's Club; 2026-05-14 third-scenario model removes land lease but excludes land opportunity cost | medium | draft | Confirm title/control, easements, covenants, and whether to charge an internal land rent |
| 84th & Nebraska Parkway full-build target is 20 L2 + 4 DCFC | operations / financial | `reports/84th_nebraska_parkway_fixed_site_analysis.md` optimization; assumes 24-post concept, 4.2 effective DCFC saturation, and 20-stall L2 saturation | low | draft | Validate with LES load quote, civil turning-radius review, and customer/traffic capture evidence |
| I-80 corridor expansion should prioritize Rock Springs WY and Elko NV first | location / strategy | v0.5.1 corridor deck revision; both are high-scoring gap-play sites, while Lincoln remains the mixed-model benchmark | low | draft | Human review required before site-owner, utility, or NEVI outreach |

## Site Configuration Assumptions

| Item | Assumed spec | Notes |
|------|-------------|-------|
| Charger count | 10 total | 8 L2 + 2 DCFC |
| L2 charger power | 7.2 kW | Standard Level 2 |
| DCFC charger power | 50–150 kW | CCS/CHAdeMO/J1772 combo; not Tesla-proprietary |
| Canopy / weather cover | Yes | Required for Nebraska winters; increases cost ~$40,000–$60,000 |
| Lighting & security cameras | Yes | Required for safety and insurance |
| Network management software | Yes | Remote monitoring, billing, reporting ~$15,000/year |
| ADA compliance | Yes | Required by code |
| Amenities (Wi-Fi, seating, retail) | TBD | Possible revenue from co-tenancy with retail; human decision needed |

## Capital Stack Assumptions (Draft)

| Item | Estimated cost |
|------|---------------|
| Land lease deposit / site prep | $50,000 |
| Electrical infrastructure / utility interconnect | $175,000 |
| L2 charger hardware (8 units) | $72,000 |
| DCFC charger hardware (2 units) | $120,000 |
| Charger installation labor | $80,000 |
| Canopy, lighting, landscaping, parking improvements | $120,000 |
| Network software setup + 1 year | $20,000 |
| Permitting, engineering, legal | $50,000 |
| Marketing / launch | $25,000 |
| Working capital / contingency (12%) | $108,000 |
| **Total** | **~$820,000–$1,000,000** |

> Note: NEVI grants (if secured) could reduce capital needed from equity/debt by $100,000–$200,000 or more depending on project scope and state award terms. §30C is not included in base-case planning for new sites because the current placed-in-service deadline is June 30, 2026.

## Review Notes

- Record changes to major assumptions in `doc/DECISIONS.md`.
- Pause for human review before using unreviewed assumptions in investor-facing or external materials.
- The utilization ramp, NEVI grant eligibility, and electricity rate (especially demand charges) are the three highest-risk assumptions and should be validated before committing capital.
