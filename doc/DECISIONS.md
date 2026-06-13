# Decisions

## Purpose

Record important project decisions and the reasoning behind them. Keep entries short and dated. Use this format:

- **Decision**: what you chose to do
- **Why**: the reasoning behind it
- **Alternatives considered**: what else you looked at (optional)
- **Status**: active / superseded / revisit by [date]

## 2026-03-29

### Stable template memory moved to `MEMORY.md`

- Decision: move the stable template and agent-memory guidance out of `README.md` and into `MEMORY.md`.
- Why: this keeps `README.md` lightweight and human-friendly while preserving a stable shared memory contract for assistants.
- Alternatives considered: keeping the stable section inside `README.md`, but that made the main project guide heavier and more confusing for new projects.
- Status: active

### README split into editable and stable sections

- Decision: make the top of `README.md` project-specific and human-facing, and keep a stable lower section for template memory and shared workflow rules.
- Why: new projects should be easy for people to customize without accidentally breaking the memory structure that assistants rely on.
- Alternatives considered: moving all stable instructions out of `README.md`, but keeping the stable section in the same file makes the boundary visible and easy to follow.
- Status: active

### README restructured for human readers

- Decision: rewrite README.md as a human-friendly project guide; move agent/memory system details out of the README.
- Why: the old README was written for AI assistants. Humans reading the repo need to understand the research workflow, directory layout, and how to track progress — not the memory system architecture.
- Alternatives considered: creating a separate MEMORY.md index file, but the existing `AGENTS.md` + `CLAUDE.md` + `.github/copilot-instructions.md` already serve that role.
- Status: active

### Dashboard prioritizes research tracking over agent config

- Decision: reorder the project website navigation to lead with Status, Decisions, and Daily Log; move Agent Rules to the end.
- Why: human researchers visiting the site care about project state and decisions first, not agent configuration.
- Status: active

### Durable memory stays in the repository

- Decision: use tracked Markdown files as the main project memory layer.
- Why: repository memory is portable across Copilot, Claude Code, Codex, GitHub, and local workflows.

### Shared instruction file is `AGENTS.md`

- Decision: use `AGENTS.md` as the cross-tool source of truth and keep thin adapter files for individual assistants.
- Why: this keeps conventions synchronized and reduces duplication.

### Research-first coding defaults

- Decision: prefer R and Python, with `.Rmd` as the default literate analysis format and `.ipynb` when interactive Python work is appropriate.
- Why: this supports reproducible research while fitting common lab workflows.
- Status: superseded by the 2026-05-13 business planning workflow.

### Large-file rule

- Decision: files larger than 100 MB should not be kept in `data/` or committed to Git. They belong in `largedata/`.
- Why: this keeps the repository lightweight, copyable, and aligned with Git hosting limits and good project hygiene.
- Status: superseded by the 2026-05-13 business planning layout; the 100 MB tracked-file limit remains active, but `data/` and `largedata/` are no longer template directories.

### HCC large-data caveat

- Decision: treat `largedata/` as working storage that fits HCC usage, not as the only copy of important large files.
- Why: inactive large files on HCC may be purged after about three months, so durable raw data should also live in a safer long-term location.
- Status: superseded by the 2026-05-13 business planning workflow.

### HCC workflow is explicit

- Decision: keep cluster execution details in dedicated Slurm scripts and preserve logs separately.
- Why: this improves reproducibility, debugging, and handoff between local and cluster execution.
- Status: superseded by the 2026-05-13 business planning workflow.

## 2026-05-13 — Volt & Go Lincoln EV Charging Station

### Business plan initiated for Lincoln, NE EV charging station

- **Decision:** Start a business plan for a public EV charging station in Lincoln, Nebraska, targeting a site near I-80 and high-end apartment communities, with 10 chargers (8 L2 + 2 DCFC) and $1M total investment.
- **Why:** Owner provided core parameters (location type, charger count, investment ceiling). This is sufficient to draft assumptions, financial model, competitive landscape, customer hypotheses, and pitch deck plan.
- **Alternatives considered:** Waiting for site identification before drafting — rejected because early financial modeling helps determine feasibility before committing to site costs.
- **Status:** Active — all documents in draft, human review in progress.

### Land lease identified as primary financial risk

- **Decision:** Flag land lease cost as the single most sensitive assumption in the financial model. At $4,500/month, the station does not reach EBITDA breakeven within 5 years. At $3,000/month or less, breakeven is achievable by Year 3.
- **Why:** The financial model makes clear that at a standard Lincoln commercial lease rate, operating costs permanently exceed projected revenues in the base scenario.
- **Alternatives considered:** (a) Assume land ownership — too speculative at this stage; (b) Assume below-market city partnership — possible but unvalidated.
- **Next action (human):** Determine whether a site can be secured at or below $3,000/month, or whether a land purchase or developer partnership is feasible.
- **Status:** Active — awaiting human decision on land strategy.

### Station brands as open-standard, all-EV-brands welcome

- **Decision:** Station will support CCS, CHAdeMO, and J1772 standards rather than joining a single proprietary network.
- **Why:** Non-Tesla EVs are the majority of the market and growing; open-standard positioning maximizes addressable customer base.
- **Alternatives considered:** Tesla network partnership — rejected because it requires proprietary hardware and limits access to non-Tesla vehicles.
- **Status:** Active.

### Candidate site recommendation: Fallbrook / Tallgrass (DRAFT, owner must validate)

- **Decision:** For v0.2, recommend a candidate site at ~7300 Tallgrass Pkwy / Fallbrook Blvd (north Lincoln, 40.881°N, -96.728°W) as the working assumption for the business plan and investor deck.
- **Why:** It is the only Class A apartment cluster in Lincoln (Brookside / Northbrook / Fallbrook development, ~1,500 units within 1 mile) with no non-Tesla DCFC within 3 miles, plus direct I-80 highway access via Exit 401 (US-34) at ~1.5 mi. The Tesla Supercharger at Hy-Vee #3 (5020 N 27th) is 2.6 mi east but Tesla-first; the only open-network DCFC (Electrify America at Casey's NW 20th) is 3.5 mi southwest.
- **Alternatives considered:** (a) Wilderness Hills / south Lincoln near US-77 — high-income but no I-80 frontage; (b) co-location at an existing Hy-Vee or Casey's — likely requires retailer partnership and gives up site control; (c) downtown / Haymarket — saturated with municipal L2 and no DCFC gap to fill.
- **Risks:** Tesla rolling out Magic Dock at Hy-Vee #3 would shrink the DCFC gap to ~2.6 mi; Electrify America siting a second Lincoln location via NEVI would weaken the "only open DCFC nearby" claim.

## 2026-05-14 — South Lincoln Alternative Scenario

### South Lincoln research scenario opened, not yet adopted

- **Decision:** Create a South Lincoln alternative scenario centered on the SouthPointe / Pine Lake / South 27th corridor, with Wilderness Hills and Village Gardens as secondary demand anchors. Build it as a comparable to the Fallbrook recommendation, not yet a replacement.
- **Why:** Owner requested a different location and a data-first reassessment with flexible stall count and capital investment. South Lincoln has stronger local retail/apartment/commuter demand than the Fallbrook I-80-access concept, but weaker NEVI corridor fit and no I-80 frontage.
- **Model result:** Base-case optimization favors **16 Level 2 stalls + 2 DCFC stalls** for maximum five-year cumulative operating EBITDA, estimated at ~$237K. None of the tested configurations recovers full capex within five years under base assumptions; operating cashflow turns positive in Y1-Y2; full capex recovery realistic at Y8-Y10.
- **Alternatives considered:** L2-only at SouthPointe (rejected — fixed OpEx eats margin); 4+ DCFC at SouthPointe (rejected — south-Lincoln DCFC demand saturates around 2.2 stalls); raw-land standalone lease in south Lincoln (rejected — same cost-structure problem that hurt the Fallbrook base case).
- **Next action (human):** (1) Contact RED Development re: a host-pad / revenue-share at SouthPointe Pavilions. (2) Request an LES written demand-charge schedule for a 16-L2 + 2-DCFC load profile. (3) Survey 20+ residents at Aventine (8801 S 33rd) and Level at Village Gardens (5701 Boboli Ln). (4) Re-run the optimization at DCFC saturation = 1.6/2.2/3.0 and L2 mature utilization = 24%/32% per the addendum in `reports/south_lincoln_location_optimization_report.md` §11.
- **Status:** Draft v0.3 — research scenario; **does not yet replace the Fallbrook v0.2 recommendation in the investor deck.**

### Section 30C tax credit treated as unavailable

- **Decision:** Both the Fallbrook and South Lincoln capital plans should treat the IRA §30C Alternative Fuel Vehicle Refueling Property Credit as **unavailable** for any new project starting in May 2026.
- **Why:** The One Big Beautiful Bill Act (signed July 2025) accelerated §30C termination to property placed in service after **2026-06-30**. Any 10-18 stall charging station starting permits now cannot be placed-in-service within ~47 days. Continuing to model the credit as a $30k-$100k upside misrepresents the capital stack to lenders and investors.
- **Alternatives considered:** (a) Keep §30C as "if available" upside — rejected because investors will inflate the implied stack; (b) Pursue a partial 6% credit — same deadline applies, still unavailable.
- **Status:** Active. Update FINANCIAL_MODEL_NOTES.md, deck slide 9 (Capital Plan), and the south Lincoln report Executive Answer to remove §30C from the capital stack.

### NEVI and IRA §30C grants included in capital plan

- **Decision:** Include potential NEVI grant ($100K–$200K) and IRA Section 30C tax credit (30% of equipment, up to $100K/item) in the capital stack model.
- **Why:** These are substantial offsets to the capital requirement and are accessible to this type of station.
- **Next action (human):** Confirm Nebraska NEVI application timeline with Nebraska DOT before relying on grant in investor deck.
- **Status:** Superseded for new work by the 2026-05-14 §30C-unavailable decision and the 2026-06-13 I-80 corridor revision. Keep NEVI as potential competitive grant funding; do not include §30C in base-case capital planning for new sites.

## 2026-06-13 — I-80 Corridor Revision

### Corridor screen prioritizes Rock Springs and Elko for first diligence

- **Decision:** Revise the I-80 corridor screen so the immediate new-site diligence list is Rock Springs, WY and Elko, NV. Keep Lincoln active as the mixed-model benchmark. Treat Iowa City, IA and Evanston, WY as watchlist opportunities unless a partner, site-control path, or live state funding window appears.
- **Why:** Rock Springs and Elko best match the corridor-gap thesis: high gap urgency plus plausible amenity anchors and NEVI corridor fit. Lincoln remains strategically important but is a mixed local-demand model rather than a pure highway gap play. Iowa City and Evanston score well but need an anchor partner or clearer grant timing before they should compete for owner attention.
- **Alternatives considered:** Pursue all four highlighted sites equally; rejected because it would dilute diligence effort and overstate the meaning of a preliminary 17+ score.
- **Status:** Draft — human review required before contacting site owners, utilities, or state NEVI offices.

### §30C excluded from I-80 corridor base case

- **Decision:** The revised I-80 corridor deck excludes IRA §30C from base-case capital planning for new sites screened in June 2026.
- **Why:** IRS guidance shows business charging property must be placed in service by June 30, 2026 to qualify under current rules. A new site starting diligence in June 2026 is unlikely to complete site control, engineering, permitting, construction, energization, and placed-in-service steps before the deadline.
- **Alternatives considered:** Keep §30C as a possible upside item; rejected because it would make the capital stack look materially easier than the current timeline supports.
- **Status:** Active assumption for corridor analysis; tax counsel should review any site-specific exception.


- Alternatives considered: documenting the rule only in Markdown, but that leaves too much room for accidental misuse.
- Status: superseded by the 2026-05-13 business planning workflow.

### Slurm wrappers should stay thin

- Decision: keep Slurm job files minimal and prefer a one-line handoff to the real Bash, Python, R, or other compute script.
- Why: this keeps resource requests and execution environment separate from scientific logic, which improves reproducibility, debugging, and reuse across local and HCC runs.
- Alternatives considered: embedding more analysis logic directly in the Slurm script, but that makes jobs harder to test and maintain.
- Status: superseded by the 2026-05-13 business planning workflow.

## 2026-04-02

### HCC software discovery order is standardized

- Decision: require HCC work to verify runtime first, obtain a compute-node allocation before doing compute work, check system-wide software with `module avail`, record the exact loaded module version, and only then fall back to `$HOME/bin` if the software is not provided by modules.
- Why: this creates a predictable order for environment setup, reduces accidental login-node work, and makes software provenance easier to reproduce across local, interactive, and batch runs.
- Alternatives considered: relying on ad hoc shell habits or checking `$PATH` first, but that makes HCC behavior less reproducible and easier to mis-document.
- Status: superseded by the 2026-05-13 business planning workflow.

## 2026-05-10

### `.Rmd` is the default literate workflow

- Decision: use `.Rmd` as the default reproducible analysis format for future projects created from this template.
- Why: the lab workflow already favors R for statistical analysis and reporting, and one default reduces startup ambiguity for humans and AI assistants.
- Alternatives considered: defaulting to `.qmd` or a mixed `.Rmd`/`.qmd` workflow, but that adds a format choice before a new project has real analysis needs.
- Status: superseded by the 2026-05-13 business planning workflow.

### `slurm-scripts/` remains the HCC script directory

- Decision: keep the directory name `slurm-scripts/`.
- Why: it is explicit, already documented across the template, and avoids a broad rename with little practical benefit.
- Alternatives considered: renaming it to `slurm/`, but the shorter name is less descriptive.
- Status: superseded by the 2026-05-13 business planning workflow.

### Minimum project metadata is standardized

- Decision: require README metadata fields for principal investigator or project lead, biological system or study domain, data owner or steward, compute environment, expected deliverables, and review status.
- Why: these fields give humans and AI assistants enough shared context to start work without over-specifying project-specific details.
- Alternatives considered: a larger metadata schema, but that would make project startup heavier than needed.
- Status: superseded by the 2026-05-13 business planning metadata.

## 2026-05-13

### Repurpose template from research to business planning

- Decision: refactor this repository from a human-in-the-loop research coding template into a human-in-the-loop business plan template. Plan recorded in `doc/BUSINESS_PLAN_TEMPLATE_REFACTOR_PLAN.md`.
- Why: the durable project-memory workflow generalizes well beyond research, and the lab needs a business-planning starter that preserves the same assumption-tracking and human-review gates. Pivoting the template is cheaper than maintaining two parallel scaffolds.
- Alternatives considered: forking into a separate `busplan-template` repo, but that would duplicate the memory contract and diverge over time; or layering business-template scaffolding on top of the research template, but that leaves HCC/Slurm/R-research surface area in place to confuse business-plan users.
- Status: active. Pre-existing research workflow decisions above were flipped to superseded as part of the refactor implementation.

### Source deck folder is `presentations/`

- Decision: store source decks under `presentations/`, not `deck/`.
- Why: the template ships two parallel decks (investor and internal); the plural name makes the multi-deck structure obvious from the directory listing.
- Alternatives considered: `deck/` (shorter, but implies a single primary deck).
- Status: active

### Drop the Node memory dashboard from the template

- Decision: remove `server.js`, `site/`, `package.json`, and `package-lock.json` from the business-plan template. Memory files stay browsable as Markdown.
- Why: the dashboard added a Node runtime dependency for a feature that mostly duplicated what reading the Markdown files already provides, and removing it keeps the template lean for non-engineer users.
- Alternatives considered: keeping the dashboard repurposed for business memory; or keeping it as an opt-in subfolder. Both add maintenance surface for marginal benefit in a planning-focused template.
- Status: active

### Retain Python utilities broadly

- Decision: keep Python in scope for the business-plan template. `scripts/log_commit.py` and `scripts/doctor.py` stay, and `requirements.txt` is retained as a real dependency manifest for financial-model checks and data cleaning.
- Why: financial models, market-data cleaning, and template health checks benefit from real Python, and the lab already has Python familiarity. A reservation for future helpers is cheaper than re-introducing Python later.
- Alternatives considered: keeping only the commit logger and doctor with no `requirements.txt`; or removing Python entirely in favor of shell or Node. Both close off financial-modeling automation we expect to want.
- Status: active

### Ship parallel investor and internal decks

- Decision: the default reporting output is two parallel deck tracks: `presentations/investor/` (pitch deck) and `presentations/internal/` (full internal business plan), sharing tokens and themes from the HTML-PPT skill but with separate narratives.
- Why: the same business plan needs both an external 10-slide investor narrative and a longer internal working document; users almost always want both eventually, and shipping them as parallel tracks from day one prevents one track from becoming an afterthought.
- Alternatives considered: investor pitch deck only (forces an internal-plan retrofit later); full internal plan only (no fundraising path); customer-discovery report only (only fits pre-product cases).
- Status: active

### Assume `html-ppt-skill` installed at the Claude Code user level

- Decision: the template assumes the `html-ppt-skill` Claude Code skill is already installed at the user level. The template does not vendor the skill and does not run an install step; the README points users to the skill's own install instructions.
- Why: vendoring duplicates the skill and creates a sync burden; an explicit npx install step adds a setup gate before a user can render anything. Assuming the skill is preinstalled keeps the template thin and lets the skill's own repo own its lifecycle.
- Alternatives considered: vendoring the skill's templates into the repo, or documenting an npx install command. Either could be revisited if the skill becomes unstable or if users routinely arrive without it.
- Status: active

### Placeholder folders carry sibling READMEs, not `.gitkeep`

- Decision: keep `assets/`, `inputs/`, and `models/` as placeholder folders, each documented by a sibling `README.md` describing its purpose (assets = deck imagery and brand assets; inputs = raw interview transcripts and market reports; models = financial spreadsheets).
- Why: empty `.gitkeep` folders accrete no usage signal; a one-paragraph README tells the next user what belongs in each folder and prevents them from sprawling into ambiguous catch-alls.
- Alternatives considered: collapsing `assets/` into `presentations/` (loses cross-deck reuse); dropping placeholders entirely (loses the convention).
- Status: active

### Keep refactor plan as a worked historical example

- Decision: once the refactor lands, leave `doc/BUSINESS_PLAN_TEMPLATE_REFACTOR_PLAN.md` in `doc/` with a "historical" banner at the top. Do not move to an archive folder, do not delete.
- Why: the plan is useful as a meta-example of how to plan a destructive refactor inside this template's memory contract, and it documents how the eight decisions were reached.
- Alternatives considered: moving to `doc/archive/` (creates a new folder for a single file); deleting in favor of git history (loses discoverability for future template users).
- Status: active

### Refactor work happens directly on `main` with staged commits

- Decision: execute the refactor on `main` as a sequence of staged commits (create new structure → rewrite docs → delete old → tooling → validate), not on a feature branch with a PR.
- Why: this is a solo template repo with no review pipeline; the destructive deletion step gets its review at the working-tree level (step 9 of the Implementation Order) rather than via PR. Direct commits keep the daily-log pairing simple.
- Alternatives considered: a `refactor/business-plan-template` branch with a PR for the review gate. Would be the right call in a multi-contributor repo; overkill here.
- Status: active

## 2026-05-14 — South Lincoln Alternative Scenario

### South Lincoln research scenario opened, not yet adopted

- Decision: create a South Lincoln alternative scenario centered on the SouthPointe / Pine Lake / South 27th corridor, with Wilderness Hills and Village Gardens as secondary demand anchors.
- Why: owner requested a different location and a data-first reassessment with flexible stall count and capital investment. South Lincoln has stronger local retail/apartment/commuter demand than the Fallbrook I-80-access concept, but weaker direct NEVI corridor fit.
- Model result: base-case optimization favors 16 Level 2 stalls + 2 DCFC stalls for maximum five-year cumulative operating EBITDA, estimated at ~$237K. None of the tested configurations recovers full capex within five years under base assumptions.
- Status: draft — human review required before changing the active deck, business plan, site recommendation, or funding narrative.

### South Lincoln deck started as separate diligence track

- Decision: start a separate South Lincoln diligence deck at `presentations/investor/volt-go-south-lincoln/` instead of overwriting the existing Fallbrook/North Lincoln investor deck.
- Why: South Lincoln has a different thesis: retail/apartment/commuter charging with likely host-site economics, not I-80/NEVI corridor positioning. Keeping decks separate prevents the active Fallbrook narrative from being accidentally replaced before owner review.
- Status: active draft — use only for internal review until site control, utility pricing, and customer demand are validated.

### South Lincoln deck revised to 16 L2 + 3 DCFC

- Decision: revise the South Lincoln deck recommendation to 16 Level 2 stalls + 3 DC fast charging stalls.
- Why: owner confirmed there is no DCFC around the South Lincoln region, so the deck now uses a revised 3.0 effective DCFC-stall demand case instead of the earlier 2.2-stall demand cap. Under that revised case, the third DCFC improves five-year operating EBITDA while the fourth DCFC remains premature.
- Status: active draft — validate with AFDC/PlugShare exports, LES demand-charge quote, host-site economics, and customer surveys before external investor or lender use.

### 84th & Nebraska Parkway owner-lot scenario opened

- Decision: create a third fixed-location scenario for the owner-controlled lot near Sam's Club at 84th Street / Nebraska Parkway, and compare it directly with Fallbrook/North Lincoln and SouthPointe/South Lincoln.
- Why: owner confirmed a specific lot and ownership/control of the land. That materially changes the economics because the model no longer carries the land lease drag that weakened the Fallbrook scenario, and the site appears physically capable of a dense 24-post concept.
- Model result: draft optimization favors 20 Level 2 stalls + 4 DCFC stalls for maximum five-year cumulative operating EBITDA, but the current deck recommendation is the lower-risk 8 L2 + 4 DCFC derisk launch: ~$934K capex, ~$305K Year 5 EBITDA, ~$904K five-year cumulative EBITDA, and ~($30K) five-year cash after capex.
- Status: active draft — requires LES utility quote, civil/turning review, parking/covenant check, and competitor export before becoming the active site strategy.

### 84th deck financial headline recalculated

- Decision: standardize the front-page and deck headline around the 8 L2 + 4 DCFC derisk-launch economics, not the 20 L2 + 4 DCFC expansion ceiling.
- Why: the exact five-year cumulative EBITDA for the derisk launch is $903,565, which rounds to **$904K**. The same build has five-year cash after capex of **($30,435)**, which rounds to **($30K)**. Showing only cumulative EBITDA was confusing because it is before capex.
- Status: active draft — keep both numbers visible together in deck and report summaries.

### 84th & Nebraska Parkway deck created as separate diligence track

- Decision: create a separate HTML-PPT deck for the owner-lot scenario at `presentations/investor/volt-go-84th-nebraska-pkwy/` instead of overwriting the Fallbrook or South Lincoln decks.
- Why: the owner-lot scenario has a materially different thesis: owned land plus vehicle-oriented retail traffic, not I-80 apartment access or SouthPointe host-site economics. A separate deck keeps the site-strategy comparison reviewable.
- Status: active draft — use for internal owner review until utility, civil, site-control, and traffic-capture assumptions are validated.
