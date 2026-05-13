# Competitive Landscape — Volt & Go Lincoln EV Charging Station

## Purpose

Track direct competitors, substitutes, customer alternatives, differentiation, and competitive risks for the Lincoln, NE EV charging station.

> **Version note:** v0.2 (2026-05-13) — populated with real Lincoln-area station data from PlugShare, ChargeHub, AFDC, and Tesla locator. All counts are **DRAFT** and must be re-verified with current AFDC data before any investor or lender use.

## Lincoln EV Charging Snapshot (May 2026)

| Metric | Value | Source |
|---|---|---|
| Total public charging ports in Lincoln | ~155 | PlugShare directory |
| Total DCFC ports in Lincoln | ~18 | ChargeHub |
| Tesla share of DCFC | 16 of ~18 ports | Tesla + AFDC |
| Non-Tesla DCFC sites | 1 (Casey's / Electrify America) | Electrify America locator |
| Largest L2 network | ChargePoint (~50 ports) | PlugShare |
| Free public ports | 2 | PlugShare |
| 2025 Lincoln DOT grant for new ports | 20 ports / $640K | City of Lincoln press release |

## Direct Competitor Register — Lincoln, NE

### DC Fast Charging (DCFC)

| Station | Address | Network | Power | Ports | Distance to candidate site | Open access? |
|---|---|---|---|---|---|---|
| Tesla Supercharger · Hy-Vee #3 | 5020 N 27th St | Tesla | up to 150 kW | 8 | ~2.6 mi E | Tesla-first (Magic Dock limited) |
| Tesla Supercharger · West O | 610 W O St | Tesla | up to 250 kW | 8 | ~5.0 mi SW | Tesla-first |
| Electrify America · Casey's | 110 NW 20th St | Electrify America | 150–350 kW (est.) | 4 | ~3.5 mi SW | Yes — CCS/CHAdeMO |

### Level 2 / Destination (selected)

| Station | Address | Network | Ports | Notes |
|---|---|---|---|---|
| Super Saver Fallbrook | 840 Fallbrook Blvd | retail / ChargePoint | L2 | Same neighborhood as candidate site |
| Russ's Market Fallbrook | 840 Fallbrook Blvd | retail | L2 | Co-located with Super Saver |
| Russ's Market 33rd & Hwy 2 | 4400 S 33rd Ct | retail | L2 | South Lincoln |
| Graduate Lincoln Hotel | 141 N 9th St | Tesla Destination | L2 | Downtown |
| Haymarket Green LES Stations | 601 P St | LES (municipal) | L2 | Downtown |
| UNL City Campus | 730 N 14th St | EV Connect | 4 ports | UNL fleet + visitors |
| UNL East Campus | 1705 Arbor Dr | EV Connect | 2 ports | UNL |
| IBEW Local #265 | 1415 Old Farm Rd | public | L2 | SW Lincoln |
| Lincoln Public Schools | various (Ada Robinson, Northeast HS, etc.) | ChargePoint | L2 | School parking — daytime |
| Garagestations Downtown (~9 garages) | Q/L/N/14th/Carriage etc. | City of Lincoln | L2 | Downtown municipal garages |

> **Verification needed:** Network identity for several stations (Casey's NW 20th and Hy-Vee #3) is inferred from public sources and should be confirmed via AFDC API before publication.

## Strategic Competitor Analysis

| Competitor | Strength | Weakness | Volt & Go counter |
|---|---|---|---|
| Tesla Supercharger (Hy-Vee 27th & West O) | Reliability, brand, Tesla-native UX, 16 of 18 DCFC ports in city | Tesla-first; non-Tesla cars use slower Magic Dock if available; no L2 dwell-time product | Open-network CCS DCFC + co-located L2 for non-Tesla overnight residents |
| Electrify America (Casey's NW 20th) | Open-network, high power | Only one Lincoln site; reliability complaints common at EA stations nationally; 5+ miles from north Lincoln apartments | Closer to Fallbrook / Northbrook residential cluster; better uptime via locally-owned operator |
| ChargePoint network (~50 L2 ports) | Largest L2 footprint; strong app | Mostly destination L2 at schools/garages/retail; not designed for long dwell-time residential charging | Dedicated residential-overnight L2 product with membership pass |
| LES Haymarket Green / Garagestations | Public, low-friction | Downtown only; no apartment-resident focus; no DCFC | Different geography + product |
| Home charging (L1/L2 in garage) | Cheapest per kWh | Unavailable to Class A apartment dwellers without garage parking | Direct substitute — this is our primary use case |
| Dealership chargers | Sometimes free | Business hours, customer-only | 24/7 public access |

## Site-Specific Competitive Gap (Candidate: Fallbrook / Tallgrass)

- **Nearest DCFC to candidate site (any network):** Tesla SC at 5020 N 27th — ~2.6 miles east.
- **Nearest non-Tesla DCFC:** Electrify America at 110 NW 20th — ~3.5 miles southwest.
- **Non-Tesla DCFC drive time from Brookside Apartments (7300 Tallgrass Pkwy):** ~10–12 min vs. ~3–4 min to candidate site.
- **L2 within 1 mile of candidate site:** Super Saver + Russ's Market on Fallbrook Blvd — retail-grade, not residential-overnight. No reserved/membership L2 product in this submarket today.

## Positioning Hypothesis (v0.2)

> "Lincoln's first open-network DCFC + reserved-overnight-L2 station purpose-built for the Fallbrook / north Lincoln apartment cluster — 3 minutes off I-80 Exit 401, all EV brands welcome, locally owned."

### Risks to the positioning

1. **Tesla opens 5020 N 27th fully to non-Tesla.** Magic Dock rollout is accelerating in 2025–2026. If Tesla retrofits adjacent stalls with universal CCS connectors, our DCFC differentiation shrinks to ~2.6 mi.
2. **Electrify America adds a second Lincoln site.** Their I-80 corridor strategy may target a Lincoln NEVI award; would erode the "only open-network DCFC nearby" claim.
3. **A property developer installs in-garage L2 at Brookside / Northbrook.** Would directly substitute the resident L2 product. Existing apartments are unlikely to retrofit, but new builds frequently include EVSE.
4. **NEVI Round 2 in Nebraska.** Could fund a competing project at a similar I-80 exit.

## Differentiation Strategy

1. **Geography:** Fallbrook is the only Class A apartment cluster in Lincoln without a non-Tesla DCFC within 3 miles. First-mover lock on this submarket.
2. **Dual product:** 8 × L2 for overnight residents + 2 × DCFC for I-80 travelers — complementary utilization curves (residential overnight, traveler midday).
3. **Open standards:** CCS + CHAdeMO + J1772 — every car works.
4. **Membership pass:** Reserved overnight L2 for Brookside / Northbrook residents at $29/mo — sticky recurring revenue.
5. **Local ownership:** Faster issue resolution than national networks; visible community accountability.
6. **Site quality:** Canopy, lighting, security cameras, restroom partnership with adjacent retail.

## Next Validation Steps

1. Pull current AFDC API for all Lincoln-area stations and confirm port counts / power ratings.
2. Drive every competitor station within 5 mi of candidate site; photograph site quality, count occupied vs. open stalls at peak times.
3. Interview 5 Brookside / Northbrook residents about current charging behavior and willingness-to-pay for reserved overnight L2.
4. Contact LES for the actual load-balancing rules and demand-charge structure at a 100 kW × 2 + 7.2 kW × 8 site.
