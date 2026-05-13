#!/usr/bin/env python3
"""Check the business plan template for common startup and handoff issues."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MAX_TRACKED_BYTES = 100 * 1024 * 1024

REQUIRED_FILES = [
    "README.md",
    "MEMORY.md",
    "AGENTS.md",
    "CLAUDE.md",
    ".github/copilot-instructions.md",
    "doc/PROJECT_STATUS.md",
    "doc/DECISIONS.md",
    "doc/DAILY_LOG.md",
    "doc/WORKLOG.md",
    "doc/ENVIRONMENT.md",
    "doc/NEW_PROJECT_CHECKLIST.md",
    "doc/BUSINESS_ASSUMPTIONS.md",
    "doc/MARKET_RESEARCH.md",
    "doc/CUSTOMER_DISCOVERY.md",
    "doc/COMPETITIVE_LANDSCAPE.md",
    "doc/FINANCIAL_MODEL_NOTES.md",
    "doc/PITCH_DECK_PLAN.md",
    "doc/BUSINESS_PLAN_TEMPLATE_REFACTOR_PLAN.md",
    "assets/README.md",
    "inputs/README.md",
    "models/README.md",
    "presentations/README.md",
    "presentations/investor/README.md",
    "presentations/internal/README.md",
    "reports/.gitkeep",
    "cache/.gitkeep",
    "scripts/log_commit.py",
    "requirements.txt",
]

REQUIRED_METADATA_LABELS = [
    "Project lead",
    "Business or venture name",
    "Target customer or buyer",
    "Market or sector",
    "Business model",
    "Data or source steward",
    "Planning stage",
    "Expected deliverables",
    "Review status",
]

REMOVED_PATHS = [
    "server.js",
    "site",
    "package.json",
    "package-lock.json",
    "deck",
    "data",
    "largedata",
    "graphs",
    "lib",
    "examples",
    "profiling",
    "slurm-log",
    "slurm-scripts",
    "scripts/run_analysis.py",
    "ai-template.Rproj",
]

ALLOWED_HISTORICAL_FILES = {
    "doc/BUSINESS_PLAN_TEMPLATE_REFACTOR_PLAN.md",
    "doc/DECISIONS.md",
    "scripts/doctor.py",
}

STALE_TERMS = [
    "HC" + "C",
    "S" + "lurm",
    "s" + "lurm",
    "wright" + "_fisher",
    "geno" + "type",
    "pheno" + "type",
]


def git_output(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=REPO_ROOT, text=True).strip()


def check(condition: bool, message: str, failures: list[str], warnings: list[str], warning: bool = False) -> None:
    if condition:
        print(f"PASS {message}")
    elif warning:
        warnings.append(message)
        print(f"WARN {message}")
    else:
        failures.append(message)
        print(f"FAIL {message}")


def file_text(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text()


def tracked_files() -> list[str]:
    return [line for line in git_output("ls-files").splitlines() if line]


def check_required_files(failures: list[str], warnings: list[str]) -> None:
    for relative_path in REQUIRED_FILES:
        check((REPO_ROOT / relative_path).exists(), f"required file exists: {relative_path}", failures, warnings)


def check_metadata_contract(failures: list[str], warnings: list[str]) -> None:
    readme = file_text("README.md")
    for label in REQUIRED_METADATA_LABELS:
        check(f"- {label}:" in readme, f"README includes metadata field: {label}", failures, warnings)


def check_reporting_contract(failures: list[str], warnings: list[str]) -> None:
    combined = "\n".join(
        file_text(name)
        for name in [
            "README.md",
            "MEMORY.md",
            "AGENTS.md",
            "CLAUDE.md",
            ".github/copilot-instructions.md",
            "doc/ENVIRONMENT.md",
            "doc/PITCH_DECK_PLAN.md",
        ]
    )
    check("html-ppt-skill" in combined, "docs mention html-ppt-skill", failures, warnings)
    check("presentations/" in combined, "docs use presentations/ for source decks", failures, warnings)
    check("deck/" not in combined, "docs no longer use deck/ as source deck folder", failures, warnings)
    check("speaker notes" in combined.lower(), "docs require speaker notes for review", failures, warnings)


def check_removed_paths(failures: list[str], warnings: list[str]) -> None:
    for relative_path in REMOVED_PATHS:
        check(not (REPO_ROOT / relative_path).exists(), f"removed path absent: {relative_path}", failures, warnings)


def check_large_tracked_files(failures: list[str], warnings: list[str]) -> None:
    try:
        files = tracked_files()
    except subprocess.CalledProcessError:
        check(False, "Git tracked-file list is available", failures, warnings, warning=True)
        return

    oversized = []
    for relative_path in files:
        path = REPO_ROOT / relative_path
        if path.exists() and path.is_file() and path.stat().st_size > MAX_TRACKED_BYTES:
            oversized.append(relative_path)

    check(not oversized, "no tracked files exceed 100 MB", failures, warnings)

    try:
        staged_files = [line for line in git_output("diff", "--cached", "--name-only").splitlines() if line]
    except subprocess.CalledProcessError:
        check(False, "Git staged-file list is available", failures, warnings, warning=True)
        return

    oversized_staged = []
    for relative_path in staged_files:
        path = REPO_ROOT / relative_path
        if path.exists() and path.is_file() and path.stat().st_size > MAX_TRACKED_BYTES:
            oversized_staged.append(relative_path)

    check(not oversized_staged, "no staged files exceed 100 MB", failures, warnings)


def check_stale_terms(failures: list[str], warnings: list[str]) -> None:
    try:
        files = tracked_files()
    except subprocess.CalledProcessError:
        check(False, "Git tracked-file list is available for stale-term check", failures, warnings, warning=True)
        return

    offenders: list[str] = []
    for relative_path in files:
        if relative_path in ALLOWED_HISTORICAL_FILES:
            continue
        path = REPO_ROOT / relative_path
        if not path.exists() or not path.is_file():
            continue
        try:
            text = path.read_text()
        except UnicodeDecodeError:
            continue
        if any(term in text for term in STALE_TERMS):
            offenders.append(relative_path)

    check(not offenders, "stale research and cluster terms only appear in historical or validation files", failures, warnings)
    if offenders:
        for relative_path in offenders:
            print(f"  stale term in: {relative_path}")


def check_daily_log_alignment(failures: list[str], warnings: list[str]) -> None:
    try:
        latest_hash = git_output("log", "-1", "--pretty=%h")
    except subprocess.CalledProcessError:
        check(False, "Git latest commit is available", failures, warnings, warning=True)
        return
    daily_log = file_text("doc/DAILY_LOG.md")
    check(latest_hash in daily_log, f"daily log mentions latest commit {latest_hash}", failures, warnings, warning=True)


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []

    print("Business plan template doctor\n")
    check_required_files(failures, warnings)
    check_metadata_contract(failures, warnings)
    check_reporting_contract(failures, warnings)
    check_removed_paths(failures, warnings)
    check_large_tracked_files(failures, warnings)
    check_stale_terms(failures, warnings)
    check_daily_log_alignment(failures, warnings)

    print("\nSummary")
    print(f"Failures: {len(failures)}")
    print(f"Warnings: {len(warnings)}")

    if failures:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
