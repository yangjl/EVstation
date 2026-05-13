# Environment Notes

## Purpose

Document how the business plan template runs locally, how presentation reporting is produced, and which tools are expected.

## Local Development

- Use the repository root as the working directory for scripts, decks, and reports.
- Keep source notes, interviews, surveys, and market exports in `inputs/`.
- Keep financial models and scenario tables in `models/`.
- Keep logos, screenshots, charts, and other presentation assets in `assets/`.
- Keep generated deliverables in `reports/`.
- Avoid committing large generated files unless they are intentional deliverables.
- Do not commit files larger than 100 MB.

## HTML-PPT Reporting

Presentation reporting should use the HTML-PPT skill:

```bash
npx skills add https://github.com/lewislulu/html-ppt-skill
```

Source decks should live in `presentations/`. Rendered decks, exported images, or shared outputs should live in `reports/`.

Authoring expectations:

- Start from an existing HTML-PPT template or layout.
- Use token-based themes and CSS variables.
- Include speaker notes for human review.
- Record major narrative or deck-structure decisions in `doc/DECISIONS.md`.

## Python And R

- Python or R may be used for repeatable data cleanup, market sizing, financial checks, or chart generation.
- Keep scripts runnable from the project root whenever possible.
- Document assumptions, inputs, outputs, and parameters near the top of each script.
- Record Python dependencies in `requirements.txt` only if dependencies are added.
- Record R environment decisions here if the project adopts R package management.

## GitHub

- Use GitHub as the authoritative history for tracked code and documentation.
- Keep heavy generated outputs out of Git unless they are deliberate deliverables.
- Write commit messages that describe the business-planning or template change clearly.
