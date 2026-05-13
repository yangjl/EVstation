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

## 2026-05-13 - business plan template refactor decisions

- Commit: `339d963` (with related commits `d957247` for the plan and `04f0866`, `0cf8da6` for log alignment)
- Summary: Recorded the decision set for refactoring this repository into a human-in-the-loop business plan template.
- Files: `doc/DECISIONS.md`, `doc/BUSINESS_PLAN_TEMPLATE_REFACTOR_PLAN.md`, `doc/DAILY_LOG.md`
- Results or impact: The template has a durable record of the business-planning direction, presentation folder choice, dual deck tracks, HTML-PPT assumption, Python utility retention, and deletion strategy.
- Next: Execute the refactor implementation under the canonical Implementation Order in `doc/BUSINESS_PLAN_TEMPLATE_REFACTOR_PLAN.md`.

## 2026-05-13 - implement business plan template refactor

- Commit: `6e2f7e7`
- Summary: Converted the active template structure and documentation to a human-in-the-loop business plan workflow.
- Files: `README.md`, `MEMORY.md`, `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `.gitignore`, `doc/`, `assets/`, `inputs/`, `models/`, `presentations/`, `scripts/doctor.py`
- Results or impact: The repository now uses business-plan memory files, presentation-oriented reporting, parallel investor/internal deck folders with slide-by-slide starter sources, and business-template validation checks. `python3 scripts/doctor.py` passes 0 failures, 0 warnings.
- Next: Start the first real business plan project by filling README metadata and the six business-plan memory docs, then author the investor and internal decks using the `html-ppt-skill`.
