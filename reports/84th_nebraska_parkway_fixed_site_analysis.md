# 84th & Nebraska Parkway Fixed-Lot EV Charging Station Analysis

**Project:** Volt & Go Lincoln  
**Location scenario:** Owner-controlled lot near Sam's Club, 84th Street / Nebraska Parkway, Lincoln, NE  
**Date:** 2026-05-14  
**Status:** Draft owner diligence. Human review required before lender, investor, permit, tax, or public use.

## Executive Answer

The 84th & Nebraska Parkway owner-lot scenario is the strongest of the three Lincoln options modeled so far. After owner feedback on derisking, the recommended launch build has been **downsized from the 20 L2 + 4 DCFC ceiling to an 8 L2 + 4 DCFC derisk launch**.

The site's structural advantages are unchanged:

- **owned land** — removes the lease drag that hurt the Fallbrook plan;
- **retail/gas/errand traffic** — Sam's Club, Walmart, Menards, Dairy Queen, and nearby restaurants create dwell-time and top-up occasions;
- **high arterial visibility** — Nebraska Parkway and S 84th carry 12-24k ADT each;
- **24-post physical concept** — the attached concept drawing supports phased L2 expansion;
- **confirmed regional DCFC gap** — supports four DCFC stalls from day one.

> **Recommended derisk launch (DOWNSIZED):** **8 Level 2 stalls + 4 DCFC stalls**
> **Estimated gross capex:** **~$934K** (−$216K vs full 20+4 ceiling)
> **Year 5 EBITDA:** **~$305K** (86% of the full-build Y5 number at 81% of the capex)
> **Five-year cumulative EBITDA:** **~$903K**
> **Five-year cash after capex:** **~($31K)** — capex effectively recovered just past Y5
> **Operating breakeven:** **Year 1** (owned-lot lower fixed OpEx)

### Why downsize from 20+4 to 8+4

All four DCFC stalls produce ~80% of operating margin in the model — so the right place to derisk is the L2 count, not the DCFC count. Going from 20 L2 to 8 L2 saves $216K of capex and only gives up $49K/yr of Y5 EBITDA, because L2 economics are dominated by demand (retail dwell + employees + light residential), not by stall count once a minimum is in place. Conduit, switchgear, and civil layout should still be engineered for the full 24-post concept so expansion to 12, 16, or 20 L2 is incremental — not a re-build.

### Comparison to other sites

| Axis | Fallbrook (8+2) | SouthPointe (16+3) | **84th derisk (8+4)** | 84th ceiling (20+4) |
|---|---:|---:|---:|---:|
| Capex | $1.0M | $953K | **$934K** | $1.15M |
| Y5 EBITDA | ($15K) | $164K | **$305K** | $354K |
| 5-yr cum EBITDA | ($206K) | $433K | **$903K** | $1,046K |
| 5-yr cash after capex | ($1.2M) | ($520K) | **($31K)** | ($104K) |
| Payback | never (model) | ~Y8-Y9 | **~Y5** | ~Y6 |

**The 84th derisk build wins on capex, Y5 EBITDA, 5-yr cumulative, and payback simultaneously** — at the lowest capex of any 4-DCFC build that the optimization model produces.

### Earlier full-build option (still valid for later expansion)

> **Full-build ceiling:** 20 L2 + 4 DCFC · ~$1.15M capex · $354K Y5 EBITDA · $1.05M 5-yr cum · ~($104K) 5-yr cash · payback ~Y6

This remains the model's operating-profit maximum and is the right target once Y2-Y3 utilization data validates the demand math. Phase 1 fallback at 12 L2 + 4 DCFC ($1.006M capex, $321K Y5) sits between the derisk launch and the full build.

## Human Review Gate

This report changes location, land economics, stall mix, capex, profitability, and site strategy. The following assumptions require owner review before external use:

- owned-lot economics and whether land opportunity cost should be charged to the project;
- 20 L2 + 4 DCFC full-build recommendation;
- 12 L2 + 4 DCFC phased-build option;
- DCFC demand saturation at about 4.2 effective stalls;
- 100 kW DCFC planning power and demand-charge treatment;
- civil feasibility of approximately 24 charging posts in the pictured lot;
- traffic capture from Sam's Club / Walmart / Menards / Nebraska Parkway.

## 1. Fixed-Site Facts

### Location And Anchors

The working site is the owner-controlled lot shown in the provided aerial concept near Sam's Club at **8480 Andermatt Dr, Lincoln, NE 68526**. Sam's official site confirms the club address and describes the location as a membership warehouse club with grocery, furniture, appliances, pickup, pharmacy, cafe, fuel station, auto/tires, and other services.

A nearby 84th & Nebraska Parkway leasing package describes the hard-corner retail/office area as having excellent visibility and names **Sam's Club, Walmart, and Menards** as retail anchors across the street.

### Traffic Anchors

City of Lincoln's 2024 ADT list gives the following nearby traffic counts:

| Road segment | ADT | Year |
|---|---:|---:|
| Nebraska Parkway, Eiger Dr to S 84th St | 24,080 | 2024 |
| Nebraska Parkway, S 84th St to S 87th St | 17,280 | 2024 |
| S 84th St, Eiger Dr to Nebraska Parkway | 16,250 | 2024 |
| S 84th St, Nebraska Parkway to Yankee Hill Rd | 12,430 | 2024 |

This is not an I-80 highway station. It is a **retail arterial / local convenience station** with a better DCFC case than SouthPointe because the lot is owned and the immediate retail node already behaves like a vehicle-oriented stop.

## 2. What The Picture Changes

The attached site concept changes the analysis in four ways:

1. **The lot is controlled by the owner.** This removes the biggest negative in the Fallbrook model: land lease cost.
2. **The site can plausibly host a dense charging field.** The concept shows approximately 24 posts, a central drive aisle, ingress/egress, and a utility/transformer zone.
3. **The surrounding uses are vehicle-oriented.** Sam's fuel, warehouse shopping, quick-service food, and big-box retail are compatible with charging.
4. **Civil feasibility is still not guaranteed.** The plan needs a turning-radius study, ADA stall layout, utility design, snow-storage review, and confirmation that back-in geometry is comfortable for pickup/SUV users.

## 3. Demand Logic

### Level 2 Demand

Level 2 works here because Sam's Club / Walmart / Menards trips create longer dwell windows than a pure gas-station stop. L2 also supports nearby employees, repeat shoppers, and drivers who want cheaper charging while doing errands.

However, L2-only is not viable. The model shows **24 L2 + 0 DCFC** remains negative over five years because the transaction value is too low for a standalone public lot with software, maintenance, snow, insurance, and security costs.

### DCFC Demand

DCFC is the main profit driver at this location. The confirmed lack of DCFC around the South/Southeast Lincoln region plus the retail/gas context supports **four DC fast chargers** as the full-build base case.

Four DCFC is materially stronger than three DCFC in the model. Five DCFC produces similar operating EBITDA, but the fifth charger adds capex, demand-charge exposure, and utility-upgrade risk before the local fast-charge market is proven.

## 4. Model Assumptions

| Assumption | Value | Notes |
|---|---:|---|
| L2 charging price | $0.38/kWh | Same as prior Lincoln planning model |
| L2 all-in electricity cost | $0.12/kWh | Includes energy and ordinary commercial cost burden |
| DCFC charging price | $0.49/kWh | Same as prior Lincoln planning model |
| DCFC all-in electricity cost | $0.22/kWh | Includes estimated demand-charge burden; must be confirmed with LES |
| L2 power | 7.2 kW | Planning assumption |
| DCFC power | 100 kW | Planning assumption; 150 kW alternative requires revised utility/capex quote |
| L2 utilization ramp | 12%, 18%, 25%, 31%, 35% | Higher than original North plan due to retail dwell and owned site |
| DCFC utilization ramp | 12%, 20%, 28%, 34%, 38% | Stronger than SouthPointe base because of retail/gas node and confirmed DCFC gap |
| L2 demand saturation | 20 stalls | Above 20, per-stall utilization begins to dilute |
| DCFC demand saturation | 4.2 stalls | Supports four DCFC; fifth starts to dilute |
| Fixed site capex | $210,000 | Existing lot reduces raw-site burden, but transformer/cabinet/civil work remains |
| L2 capex per stall | $18,000 | Hardware, pedestal, wiring, installation share |
| DCFC capex per stall | $145,000 | Hardware, installation, interconnect share |
| Extra utility step-up | $75,000 if 5+ DCFC | Placeholder for larger utility upgrade |
| Fixed OpEx | $52,000/year | Network/admin/security/snow/insurance/base overhead |
| Maintenance | $1,600/L2/year; $9,000/DCFC/year | Same maintenance convention as South Lincoln report |

## 5. Stall-Mix Optimization

| Configuration | Gross capex | 5-year cumulative EBITDA | Cash after capex | Year 5 EBITDA | Interpretation |
|---|---:|---:|---:|---:|---|
| 0 L2 + 4 DCFC | $790,000 | $808,825 | **$18,825** | $271,510 | Best strict five-year cash payback, but underuses the lot and loses dwell/member product |
| 4 L2 + 4 DCFC | $862,000 | $856,196 | ($5,804) | $288,069 | Near five-year payback; limited L2 usefulness |
| 8 L2 + 4 DCFC | $934,000 | $903,565 | ($30,435) | $304,627 | Capital-efficient balanced phase |
| **12 L2 + 4 DCFC** | **$1,006,000** | **$950,935** | **($55,065)** | **$321,185** | Recommended Phase 1 if owner wants lower execution risk |
| 16 L2 + 4 DCFC | $1,078,000 | $998,304 | ($79,696) | $337,743 | Strong full build |
| **20 L2 + 4 DCFC** | **$1,150,000** | **$1,045,674** | **($104,326)** | **$354,301** | Best five-year operating-profit build within 24-post concept |
| 24 L2 + 0 DCFC | $642,000 | ($55,151) | ($697,151) | $24,391 | L2-only fails |
| 16 L2 + 3 DCFC | $933,000 | $731,099 | ($201,901) | $256,866 | Lower capex, but under-monetizes DCFC gap |
| 20 L2 + 3 DCFC | $1,005,000 | $778,467 | ($226,533) | $273,424 | Extra L2 does not replace fourth DCFC |
| 18 L2 + 5 DCFC | $1,334,000 | $1,039,431 | ($294,569) | $354,998 | Similar EBITDA to 20+4, much worse capital recovery |
| 22 L2 + 2 DCFC | $896,000 | $495,262 | ($400,738) | $189,346 | Too L2-heavy and DCFC-light |

### Interpretation

- If the owner wants **maximum operating profit**, build toward **20 L2 + 4 DCFC**.
- If the owner wants **best five-year cash payback**, a smaller **4 DCFC-only** build wins mathematically, but it is too narrow strategically and does not use the 24-post lot concept.
- If the owner wants a **financeable phased plan**, start with **12 L2 + 4 DCFC** and pre-build conduit / switchgear / layout for 20 L2 + 4 DCFC.

## 6. Annual EBITDA For Recommended Full Build

**Recommended full build:** 20 L2 + 4 DCFC  
**Gross capex:** ~$1.15M

| Year | Modeled EBITDA | Cumulative EBITDA | Cumulative cash after capex |
|---|---:|---:|---:|
| Y1 | $32,887 | $32,887 | ($1,117,113) |
| Y2 | $128,251 | $161,138 | ($988,862) |
| Y3 | $226,896 | $388,034 | ($761,966) |
| Y4 | $303,339 | $691,373 | ($458,627) |
| Y5 | $354,301 | $1,045,674 | ($104,326) |

The project nearly recovers gross capex within five years before any terminal value, refinance, debt structure, tax effects, or grants. That is materially stronger than the previous North and South scenarios.

## 7. Comparison With Other Lincoln Options

| Axis | Fallbrook / North Lincoln | SouthPointe / South Lincoln revised | 84th & Nebraska Parkway owner lot |
|---|---|---|---|
| Site strategy | Standalone lease near I-80 and apartments | Retail-host South Lincoln DCFC gap | Owned lot near Sam's / Walmart / Menards |
| Recommended build | 8 L2 + 2 DCFC | 16 L2 + 3 DCFC | **20 L2 + 4 DCFC** |
| Gross capex | ~$1.0M | ~$953K | ~$1.15M |
| Year 5 EBITDA | ~($15K) | ~$164K | **~$354K** |
| 5-year cumulative EBITDA | ~($206K) | ~$433K | **~$1.05M** |
| 5-year cash after capex | ~($1.21M) | ~($520K) | **~($104K)** |
| Main advantage | I-80 access | South Lincoln DCFC gap, local demand | Owned land + retail/gas node + 24-post fit |
| Main risk | Lease drag and nearby competitors | Host-site terms not controlled | Civil/utility feasibility and actual traffic capture |

### Ranking

1. **84th & Nebraska Parkway owner lot** — best modeled economics and strongest site-control advantage.
2. **SouthPointe / South Lincoln** — good local demand but weaker because host economics and utility terms are not controlled.
3. **Fallbrook / North Lincoln** — weakest base-case economics unless land is owned or lease/partnership terms materially improve.

## 8. Recommended Build Strategy

### Preferred Full Build

**20 L2 + 4 DCFC**

Use this if the owner is comfortable with a roughly **$1.15M** gross capex plan and can get a favorable LES load quote.

Why this is best:

- Four DCFC stalls monetize the confirmed fast-charging gap.
- Twenty L2 stalls use the lot's 24-post density without overbuilding beyond the modeled L2 saturation point.
- Owned land shifts the project from a long-payback infrastructure experiment to a near-five-year capital-recovery asset.
- The fourth DCFC is accretive; the fifth is not capital-efficient yet.

### Lower-Risk Phase 1

**12 L2 + 4 DCFC**

Use this if the owner wants to stage capital:

- capex drops to about **$1.006M**;
- Year 5 EBITDA remains strong at about **$321K**;
- five-year cash after capex is about **($55K)**, slightly better than the full 20+4 plan because less capital is deployed;
- the site can later expand L2 count if utilization validates.

## 9. Critical Diligence Before Construction

1. **LES utility quote:** confirm transformer size, demand charges, line-extension responsibility, service timing, and whether 4 x 100 kW DCFC plus 20 L2 is feasible without a major off-site upgrade.
2. **Civil/traffic review:** verify turning radius, back-in geometry, ADA placement, snow storage, fire access, and whether customer circulation conflicts with nearby restaurant / Sam's traffic.
3. **Site control documentation:** confirm the project entity owns or controls the lot and whether any easements, cross-access agreements, or parking covenants restrict EV charging.
4. **Competitive export:** pull AFDC / PlugShare around 84th & Nebraska Parkway to document the no-DCFC claim and the nearest Tesla/open-network DCFC distances.
5. **Retail capture test:** observe Sam's/Walmart/Menards traffic for two peak windows and survey 30 drivers about charging willingness during errands.
6. **Vendor quote:** price 100 kW vs 150 kW DCFC; if 150 kW materially raises demand charges, keep the model at 100 kW or add battery buffering.

## 10. Bottom Line

This fixed owner-lot location should become the new leading site scenario unless utility/civil review finds a major blocker.

The owner's lot solves the biggest structural problem in the earlier plans: land economics. It also supports more DCFC than the first South Lincoln scenario because the site sits in a vehicle-oriented retail cluster rather than only a dwell-time retail center.

**Recommended decision:** advance 84th & Nebraska Parkway to formal 60-day diligence with an **8 L2 + 4 DCFC derisk launch target** (~$934K capex). Engineer civil, conduit, and switchgear for the full 24-post concept so later expansion to 12, 16, or 20 L2 is incremental. The 20 L2 + 4 DCFC ceiling remains the long-term operating-profit target; commit only after Y2-Y3 utilization validates demand.

## Sources

- City of Lincoln, **Average Daily Traffic Volume**, 2024 listing: https://www.lincoln.ne.gov/City/Departments/LTU/Transportation/Traffic-Engineering/Average-Daily-Traffic-Volume
- Sam's Club official store page, **Lincoln Sam's Club #4873**, 8480 Andermatt Dr: https://www.samsclub.com/club/4873-lincoln-ne
- Cushman & Wakefield / Lund listing package, **84th & Nebraska Parkway**, retail anchor context: https://s3.us-east-2.amazonaws.com/media.myelisting.com/listings/11/294845/84thnebraskaparkwaylincolnmarketingpackage-XZj-SAg.pdf
- Nebraska Department of Water, Energy, and Environment, **Annual State Energy Report 2025**: https://dwee.nebraska.gov/forms/publications-grants-forms/26-001
- U.S. DOE AFDC, **Electric Vehicle Charging Station Locations**: https://afdc.energy.gov/fuels/electricity-locations
