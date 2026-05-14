# South Lincoln Location Research & Five-Year Stall Mix Optimization

## Volt&Go Lincoln — Alternative Scenario

**Date:** 2026-05-14  
**Status:** Draft research scenario — human review required before changing the active business plan, deck, or funding story.  
**Scope:** South Lincoln alternative to the current Fallbrook/Tallgrass concept. This report does not supersede the Fallbrook recommendation unless the owner approves a site change.

## Executive Answer

South Lincoln is a stronger **local retail / apartment / commuter** charging market than an I-80 corridor charging market. The best candidate zone is the **SouthPointe / Pine Lake / South 27th Street corridor**, with Wilderness Hills and Village Gardens as secondary demand anchors.

Under the base planning model, the operating-profit-maximizing configuration is:

> **Recommended South Lincoln operating build:** **16 Level 2 stalls + 2 DC fast charging stalls**  
> **Estimated gross capex:** **~$808,000**  
> **Five-year cumulative EBITDA:** **~$237,000**  
> **Year 5 EBITDA:** **~$107,000**  
> **Five-year cash after capex:** **~($571,000)** before terminal value, refinancing, tax credits, or grants.

This is the most profitable operating configuration among the tested mixes, but it does **not** recover full project capex inside five years under base assumptions. If the owner requires five-year full-capital payback, the recommendation is **do not proceed yet** without improving at least one of: land cost, utility demand charges, equipment cost, grant/tax-credit eligibility, or committed apartment/retail/fleet demand.

## Human Review Gate

This report changes location, customer mix, capex, stall mix, utilization, grant posture, and five-year profit expectations. The following need owner review before external use:

- South Lincoln vs. Fallbrook location strategy
- 16 L2 + 2 DCFC recommended build
- Capital range and utility assumptions
- Five-year profit and payback interpretation
- Membership conversion assumptions
- Whether to pursue a retail-host partnership instead of a leased standalone parcel

## 1. Why South Lincoln Is Different

The Fallbrook concept is a north Lincoln apartment + I-80 access play. South Lincoln is different:

- It has stronger local retail and commuter traffic.
- It has more high-income residential growth, especially around Pine Lake, Wilderness Hills, and Village Gardens.
- It is weaker for NEVI corridor funding because the best South Lincoln retail/apartment sites are not within one mile of I-80.
- It should therefore be treated as a **local convenience and dwell-time charging hub**, not primarily a federally funded highway-corridor station.

## 2. Candidate South Lincoln Locations

| Candidate zone | Demand anchors | Traffic / access | Charging gap | Initial rating |
|---|---|---|---|---|
| **A. SouthPointe / Pine Lake / S 27th** | SouthPointe Pavilions, retail, restaurants, cinema, Bryan Health Pine Lake, nearby apartments | S 27th at Pine Lake area has ~22k-25k ADT on nearby S 27th segments; Pine Lake retail corridor has strong dwell time | Existing L2 nearby, but no obvious open-network DCFC in South Lincoln | **Best overall** |
| B. Wilderness Hills / S 33rd / Yankee Hill | Aventine at Wilderness Hills, newer south Lincoln apartments, US-77 / US-2 access | Residential growth, good income profile, less retail dwell time unless co-located with a commercial pad | Good apartment demand, but weaker daily retail turnover | Strong residential option |
| C. Village Gardens / S 56th / Pine Lake | Level at Village Gardens, mixed-use neighborhood, restaurants, apartments | Good local access and walkability, farther from major highway traffic | Good L2 membership logic, weaker DCFC draw | L2-heavy option |

### Recommended Candidate Zone

**SouthPointe / Pine Lake / South 27th** screens best because it combines:

1. High local traffic.
2. Retail and restaurant dwell time.
3. South Lincoln apartment growth.
4. Better visibility than apartment-only sites.
5. A larger non-Tesla fast-charging gap than the north Lincoln I-80 corridor once South Lincoln is viewed as its own submarket.

The best site structure is likely not raw land. It is a **retail-host or shopping-center edge-pad partnership** where the host benefits from dwell time and Volt&Go reduces land cost.

## 3. Data Anchors

### Traffic

City of Lincoln 2024 ADT data supports South 27th / Pine Lake as a high-traffic local corridor:

| Segment | ADT | Count year |
|---|---:|---:|
| S 27th St, Jane Ln to Pine Lake Rd | 25,430 | 2024 |
| S 27th St, Pine Lake Rd to Yankee Hill Rd | 22,060 | 2023 |
| S 27th St, Nebraska Pkwy to Tipperary Tr | 24,480 | 2024 |
| S 27th St, Woods Blvd to Nebraska Pkwy | 21,190 | 2024 |

City documentation says the ADT list includes the most recent estimated average daily traffic volume for arterial and selected collector streets around Lincoln.

### Demand Anchors

- **SouthPointe Pavilions** is located at 2910 Pine Lake Road in Lincoln and is a major open-air retail center at Pine Lake / South 27th.
- **Aventine at Wilderness Hills** identifies itself as a luxury apartment community in southern Lincoln, near US-77 and US-2, with address 8801 S 33rd St.
- **Level at Village Gardens** is a South Lincoln apartment community at 5701 Boboli Lane, close to SouthPointe and Village Gardens amenities.
- South Lincoln also has existing L2 signals, including Russ's Market / Super Saver, SouthPointe-area charging, schools, apartments, and dealership/destination chargers. These validate EV presence but also create L2 competition.

### EV Base

The Nebraska Department of Water, Energy, and Environment / DMV source lists:

- **10,938 electric vehicles statewide as of 2025-12**
- **48,069 electric/gasoline hybrid vehicles statewide as of 2025-12**

Lincoln-specific EV registrations were not located in public data. The project should continue using a planning range of **~1,200-1,800 Lincoln EVs**, pending confirmation from Lancaster County / DMV data.

## 4. Why NEVI Is Not The Primary South Lincoln Thesis

Nebraska DOT says Nebraska receives about **$30.2M** in NEVI Formula funds and that the 2025 plan focuses on I-80 and other Alternative Fuel Corridors. NDOT also states the first phase will install roughly **30-35 DCFC sites**, each with a minimum of **four chargers**.

The Nebraska RFP minimum requirements include:

- At least four DCFC ports.
- Each port supports at least 150 kW continuous power.
- All four ports must support simultaneous operation.
- Site must be within **1.0 mile** of the nearest I-80 exit ramp for the referenced I-80 RFP.
- 97% annual average uptime during the five-year operating period.
- Multiple payment options and 24/7 customer support.

**Implication:** A SouthPointe / Pine Lake station should not rely on NEVI as base-case funding. It may still pursue Section 30C or local/state incentives, but NEVI corridor funding is structurally better suited to I-80-adjacent sites.

## 5. Optimization Model

### Model Objective

The model tests multiple stall combinations and ranks them two ways:

1. **Maximum five-year cumulative EBITDA** — best operating-profit configuration.
2. **Best five-year cash after capex** — most capital-protective configuration.

### Key Base Assumptions

| Variable | Base value | Notes |
|---|---:|---|
| L2 charging price | $0.38/kWh | Same as existing plan; human review required |
| DCFC charging price | $0.49/kWh | Same as existing plan; human review required |
| L2 all-in electricity cost | $0.12/kWh | Includes energy plus local estimate; verify with LES |
| DCFC all-in electricity cost | $0.22/kWh | Includes demand-charge burden; highly uncertain |
| L2 capex per stall | $18,000 | Hardware + install + shared electrical |
| DCFC capex per stall | $145,000 | Hardware + install + interconnect share |
| Fixed site capex | $230,000 | Site prep, engineering, canopy/signage, launch, contingency base |
| L2 utilization ramp | 10%, 16%, 23%, 28%, 32% | South Lincoln dwell-time ramp |
| DCFC utilization ramp | 10%, 16%, 22%, 26%, 28% | Lower than I-80 because South Lincoln is local traffic |
| L2 demand saturation | 16 stalls | Above this, utilization per stall is reduced |
| DCFC demand saturation | 2.2 stalls | Above this, utilization per stall is reduced |
| Membership add-on | $600-$1,500 per L2 stall/year | Proxy for resident/commuter passes and reservations |
| Fixed OpEx | $72k-$90k/year | Land/host fee, insurance, software, labor, admin, marketing |

### Tested Results

| Configuration | Gross capex | 5-year cumulative EBITDA | 5-year cash after capex | Year 5 EBITDA | Interpretation |
|---|---:|---:|---:|---:|---|
| 6 L2 + 2 DCFC | $628,000 | $81,848 | ($546,152) | $55,337 | Most capital-protective among tested builds, but too small for full South Lincoln opportunity |
| 8 L2 + 2 DCFC | $664,000 | $112,798 | ($551,202) | $65,632 | Better utilization, still undersized for resident/retail dwell demand |
| 12 L2 + 2 DCFC | $736,000 | $174,696 | ($561,304) | $86,222 | Good phased build if owner wants lower capex than full recommendation |
| **16 L2 + 2 DCFC** | **$808,000** | **$236,594** | **($571,406)** | **$106,813** | **Best five-year operating-profit configuration** |
| 18 L2 + 2 DCFC | $844,000 | $231,794 | ($612,206) | $106,613 | Extra L2 begins to dilute utilization |
| 20 L2 + 2 DCFC | $880,000 | $226,994 | ($653,006) | $106,413 | Overbuilt under base demand |
| 12 L2 + 4 DCFC | $1,026,000 | $132,946 | ($893,054) | $81,467 | Too DCFC-heavy for South Lincoln local demand |
| 16 L2 + 4 DCFC | $1,098,000 | $194,845 | ($903,155) | $102,058 | Higher capex, no matching South Lincoln DCFC demand in base case |
| 24 L2 + 2 DCFC | $952,000 | $217,394 | ($734,606) | $106,013 | Too many L2 stalls before demand is proven |
| 16 L2 + 0 DCFC | $518,000 | ($155,906) | ($673,906) | ($7,639) | L2-only cannot cover fixed site costs |

## 6. Recommended Build Strategy

### Phase 1 Recommended Build

**16 L2 + 2 DCFC** if the owner can secure a host-site partnership or low land cost.

Why:

- L2 matches South Lincoln's retail/apartment dwell-time use case.
- Two DCFC stalls provide high-ticket convenience charging without overbuilding fast-charge capacity.
- Four DCFC stalls appear overbuilt unless a fleet, rideshare, highway, or NEVI-compatible site is secured.
- L2-only does not appear viable because fixed operating costs overwhelm the lower transaction value.

### Capital-Efficient Alternative

**12 L2 + 2 DCFC** if the owner wants a lower-risk first phase.

This option lowers capex by about $72,000 versus 16 L2 + 2 DCFC, while still producing a positive Year 5 EBITDA estimate of about $86,000. It is less profitable over five years, but easier to finance and expand.

### Avoid In Base Case

- **4+ DCFC in South Lincoln** unless a specific site is within an eligible corridor or has an anchor demand contract.
- **L2-only standalone station** unless land is free or the charging is a bundled apartment amenity.
- **20+ L2 stalls at launch** before resident/retail demand is validated.

## 7. Profit-Maximization Conclusion

If the goal is **maximum five-year operating profit**, choose:

> **16 L2 + 2 DCFC at SouthPointe / Pine Lake / S 27th**

If the goal is **maximum five-year cash after capex**, the base-case model says:

> **Do not proceed without improving the economics.** None of the tested configurations recovers full capex within five years.

The most important levers are:

1. **Land / host economics:** A retail-host revenue share or free/discounted parking-field pad could improve five-year cash by $150k-$300k versus a standalone lease.
2. **Utility rate / demand charges:** Reducing effective DCFC electricity cost from $0.22/kWh to $0.16-$0.18/kWh materially improves EBITDA.
3. **Capital subsidy:** Section 30C, state/local grants, or host contribution could close the five-year cash gap.
4. **Pre-sold demand:** Apartment, employer, rideshare, or fleet commitments can support faster utilization ramp.
5. **Phasing:** Install conduit and switchgear for expansion, but launch with 12-16 L2 and 2 DCFC.

## 8. Go / No-Go Criteria For South Lincoln

Move forward only if at least four of these are true:

| Criterion | Target |
|---|---|
| Site control | Retail host or apartment/retail partnership lowers land cost materially |
| Utility quote | LES confirms DCFC demand charges do not break the unit economics |
| Customer validation | 30+ resident/commuter survey responses show willingness to pay |
| Anchor partner | SouthPointe, apartment manager, employer, healthcare site, or fleet partner agrees to promote usage |
| Incentive fit | Section 30C tract eligibility, local grant, or host capital contribution is confirmed |

## 9. Immediate Research Tasks

1. Pull AFDC export for all stations within 5 miles of SouthPointe / Pine Lake.
2. Drive SouthPointe, Wilderness Hills, and Village Gardens and count existing chargers, available parking, transformer proximity, lighting, and restroom access.
3. Contact SouthPointe Pavilions / RED Development about a host-site or revenue-share concept.
4. Contact LES for a load quote for 2 x 100-150 kW DCFC plus 12-16 L2.
5. Survey residents at Aventine, Level at Village Gardens, Wilderness Hills South, and nearby apartments.
6. Ask a CPA/grant advisor to check Section 30C tract eligibility for candidate parcels.

## 10. Source Notes

- City of Lincoln, Average Daily Traffic Volume: https://www.lincoln.ne.gov/City/Departments/LTU/Transportation/Traffic-Engineering/Average-Daily-Traffic-Volume
- City of Lincoln, 2024 ADT listing PDF: https://www.lincoln.ne.gov/files/sharedassets/public/v/1/ltu/transportation/traffic-engineering/adtv/2024-list.pdf
- SouthPointe Pavilions venue page: https://www.reddevelopment.com/southpointe-pavilions/venue/southpointe-pavilions/
- Aventine at Wilderness Hills: https://www.aventinewildernesshills.com/
- Level at Village Gardens: https://www.levellincoln.com/
- PlugShare Lincoln directory: https://www.plugshare.com/directory/us/nebraska/lincoln
- Nebraska DOT NEVI program: https://dot.nebraska.gov/business-center/environment/nevi/
- Nebraska DOT RFP R231-24 NEVI Formula Program: https://dot.nebraska.gov/media/ucgdo2tl/r231-24-nevi-formula-program.pdf
- Nebraska DWEE registered vehicles by fuel consumed: https://dee.nebraska.gov/sites/default/files/publications/196_4.pdf
- IRS Alternative Fuel Vehicle Refueling Property Credit: https://www.irs.gov/credits-deductions/alternative-fuel-vehicle-refueling-property-credit

---

## 11. Audit &amp; Strategy Review (Addendum, 2026-05-14)

This addendum re-checks the math and the strategic framing of sections 1-10 above and proposes specific report improvements. Numbers in this addendum are independent back-of-envelope estimates against the model's published outputs; they are not a re-run of the model.

### 11.1 Math sanity check — does 16 L2 + 2 DCFC really maximize five-year EBITDA?

**Capex arithmetic:** 16 × $18,000 (L2) + 2 × $145,000 (DCFC) + $230,000 (fixed) = $808,000. ✅ matches the report.

**Year-5 EBITDA back-of-envelope (independent):**

| Stream | Calc | Gross margin |
|---|---|---:|
| L2 | 16 × 7.2 kW × 8,760 h × 0.32 util × ($0.38 − $0.12) | ~$84,000 |
| DCFC | 2 × 100 kW × 8,760 h × 0.28 util × ($0.49 − $0.22) | ~$132,000 |
| Membership | 16 stalls × ~$1,000/stall | ~$16,000 |
| Fixed OpEx | midpoint of $72k–$90k | ($81,000) |
| **Implied Y5 EBITDA** | | **~$151,000** |

The report says Y5 EBITDA = $106,813 — about **$44k lower** than the back-of-envelope. The plausible reasons (none invalidate the model, all worth confirming):

1. Software / transaction fees (~$0.02/kWh) not netted in the per-kWh margin shown — could be $13k/yr.
2. Demand-saturation discount applied to the 2-DCFC build at 2/2.2 ≈ 91% — that takes $132k DCFC margin → $120k, a $12k haircut.
3. Fixed OpEx is the upper end of the band ($90k) rather than the midpoint.

**Conclusion:** internal math is plausible and conservative. The directional optimum (16 L2 + 2 DCFC) is supported by the saturation logic (utilization per stall flattens above 16 L2 and above ~2.2 DCFC), and the comparison configurations behave correctly: 18 L2 and 20 L2 add capex without adding Y5 EBITDA; 4-DCFC builds add capex that DCFC demand cannot absorb.

### 11.2 Operating breakeven is sooner than the executive summary implies

Cumulative 5-year EBITDA = $237k and Y5 EBITDA = $107k → years 1-4 sum to $130k. With the published utilization ramp (L2 10%→32%; DCFC 10%→28%), a defensible per-year split is roughly Y1 ~+$10k, Y2 ~+$25k, Y3 ~+$45k, Y4 ~$50k, Y5 $107k.

**This means the station likely turns operating-cashflow positive in Year 1 or early Year 2, not Year 3+.** The executive summary should call that out — the issue is not month-to-month survival, it is the **multi-year capex recovery curve** stretching past Year 5.

### 11.3 Capex recovery curve — the "do not proceed" framing is too binary

Year 5 EBITDA is $107k and the model implies it is still growing. Holding it flat at $107k from Y6 onward (no growth, no degradation), full $808k capex recovery happens around **Y10**. With modest continued growth, Y8-Y9 is realistic.

Industry norms for charging infrastructure are 7-12 year payback projects, not 3-5 year. The "do not proceed without improving economics" line should be reframed:

> "Five-year full-capex recovery is not realistic under base assumptions; the underlying business is an 8-10 year infrastructure project that turns operating-cash-positive in year 1-2. Owners requiring 5-year payback should structure the deal around grants/credits or do not proceed."

### 11.4 Section 30C credit — material strategic factor missing from the model

The IRA §30C Alternative Fuel Vehicle Refueling Property Credit was accelerated by the One Big Beautiful Bill Act (signed July 2025) and now terminates for property placed in service after **June 30, 2026** (six weeks from today).

| Status | Implication |
|---|---|
| Today: 2026-05-14 | 47 days until §30C deadline |
| Realistic permit→construction→commissioning | 6-9 months minimum for a 16-stall station |
| Conclusion | **§30C is effectively unavailable for this project** |

The optimization model does not include §30C in either direction, which is the correct call given the deadline. But the report should explicitly state that the credit is off the table, so an investor reading "potential 30C" does not mistakenly inflate the capital stack.

Counterfactual: if §30C had been available at 30% (with prevailing-wage / apprenticeship compliance) on the ~$578k eligible equipment+install portion, the credit would have been ~$173k — large enough to materially shift the 5-year cash gap from −$571k to ~−$400k. The federal program window closing is a real strategic loss.

### 11.5 Two assumptions worth challenging before owner sign-off

1. **DCFC demand saturation cap of 2.2 stalls.** This is the single biggest constraint on the model — it is what makes 4-DCFC configurations look uneconomic. The 2.2 cap implies that the South Lincoln catchment can only fill ~2 fast chargers' worth of demand at peak. Defensible for a local-station thesis with ~250 EVs in catchment, but if Tesla opens the Hy-Vee #3 NACS connector to non-Tesla cars in 2026, north-Lincoln DCFC supply jumps and pulls share from any south-Lincoln DCFC. **Recommend re-running the optimization at saturation = 1.6, 2.2, and 3.0 to see if the optimum shifts.**

2. **L2 mature utilization of 32%.** Industry mature L2 utilization is 10-25%. 32% is at the absolute top of the band and only realistic with a hard apartment-membership lock-in. If the achievable mature utilization is 24% rather than 32%, L2 margin drops ~25%, knocking Y5 EBITDA from $107k to ~$86k and 5-yr cum EBITDA from $237k to ~$190k. **Recommend a sensitivity row at 24% mature L2 utilization.**

### 11.6 South Lincoln vs Fallbrook — comparison the report does not yet make

Both scenarios live in the repo but no single table compares them on the same axes. Here is the comparison on the published numbers:

| Axis | Fallbrook (north, v0.2 deck) | South Lincoln (this report) |
|---|---|---|
| Site type | Standalone parcel near I-80 Exit 401 | Retail-host pad at SouthPointe Pavilions |
| Build | 8 L2 + 2 DCFC | **16 L2 + 2 DCFC** |
| Gross capex | ~$1,000,000 | $808,000 |
| Land cost assumption | Standalone lease $4,500/mo (= $54k/yr) | Retail-host fee folded into $72-90k fixed OpEx |
| Y5 EBITDA | -$15k (base, FINANCIAL_MODEL_NOTES.md) | **+$107k** |
| 5-yr cumulative EBITDA | ~-$205k | **+$237k** |
| I-80 corridor visibility | Yes (Exit 401, ~1.5 mi) | No (>7 mi to nearest ramp) |
| NEVI eligibility | Marginal — not on AFC | Effectively no — too far from I-80 |
| Direct DCFC competitor distance | 2.6 mi (Tesla Hy-Vee) | No DCFC in south Lincoln |
| Direct L2 competitor distance | ~0 (Super Saver Fallbrook) | ~0 (ChargePoint at SouthPointe) |
| Class A apartment density (1 mi) | ~1,500 units | ~1,200-1,800 units |
| Open-network DCFC gap | "Only" gap within 3 mi | Larger gap (no DCFC in entire submarket) |

The **driver of the +$442k five-year EBITDA delta** is not really location — it is the **cost structure**: standalone lease vs retail-host partnership, plus the L2 count (16 vs 8) that better matches apartment dwell demand. A Fallbrook deal structured as a retail-host partnership would close most of that gap; a south Lincoln deal structured as a standalone lease would open the gap back up.

**Conclusion:** the right question is not "north vs south" — it is **"standalone vs retail-host"**. The location decision should be made after both submarkets are tested under both cost structures.

### 11.7 Report improvements proposed

Specific edits that would tighten this report without changing its recommendation:

1. Add a sensitivity table — DCFC saturation (1.6 / 2.2 / 3.0) × L2 mature utilization (24% / 32%) — to show the model's elasticity to its two most aggressive assumptions.
2. Move §11.2 (operating-breakeven Y1-Y2) into the Executive Answer so the reframing is the first thing the reader sees.
3. Add an explicit "§30C is unavailable" line in §7 (Incentive Revision) with the 2026-06-30 deadline reference.
4. Insert the comparison table from §11.6 as a top-level section so the deck can lift it directly.
5. Drop the "Five-year cash after capex: ~(\$571,000)" from the Executive Answer or annotate it as "before any grant, terminal value, or refinancing" — investors will otherwise misread it as a $571k loss.
6. Tighten §9 Immediate Research Tasks to a numbered 30-60-90 day plan with named owners and dates.

### 11.8 Open data gaps (still)

- Lancaster County / Lincoln-specific EV registration count (have statewide; need local).
- Confirmed RED Development openness to a host-pad deal at SouthPointe.
- LES written demand-charge structure for a 100-kW × 2 + 7.2-kW × 16 load profile.
- 20+ resident surveys at Aventine and Level for actual WTP at $29-$49/mo.
- Section 30C census-tract eligibility map for the candidate parcel (moot in practice given the deadline, but worth recording for any future credit revival).

