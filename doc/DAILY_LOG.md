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

## 2026-05-13 - First investor HTML pitch deck built (v0.1 DRAFT)

- Commit: (pending)
- Summary: Generated initial 11-slide HTML investor pitch deck for Volt & Go Lincoln using the `html-ppt-skill` `pitch-deck` template. Pulled content from PITCH_DECK_PLAN.md, FINANCIAL_MODEL_NOTES.md, COMPETITIVE_LANDSCAPE.md, and CUSTOMER_DISCOVERY.md.
- Files: `presentations/investor/volt-go-lincoln/index.html`, `presentations/investor/volt-go-lincoln/style.css`
- Result: Browser-renderable deck with speaker notes on every slide. Marked as DRAFT v0.1 in cover footer. Slides flagged for human review: Customers (unvalidated hypotheses), Market (numbers need validation), Business Model (pricing), Financials (land-lease sensitivity), Capital Plan (grants unverified), The Ask (terms TBD).
- Next concrete step: Owner reviews deck content against PITCH_DECK_PLAN.md "Key Slides Requiring Human Review" list before any external use.

## 2026-05-13 - Volt & Go Lincoln EV charging station business plan drafted

- Commit: (pending — commit after human review)
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
