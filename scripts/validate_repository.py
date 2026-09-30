from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

required = [
    "README.md",
    "templates/weekly-brief-template.md",
    "sources/source-register.md",
    "strategy/opportunity-tracker.md",
    "strategy/competitor-watch.md",
    "strategy/implications-for-oradigit.md",
    "briefs/2026/2026-09-14-weekly-brief.md",
    "briefs/2026/2026-09-21-weekly-brief.md",
    "briefs/2026/2026-09-28-weekly-brief.md",
    "briefs/2026/2026-10-05-weekly-brief.md",
    "topics/pet-ct/README.md",
    "topics/cardiac-ct-ccta/README.md",
    "topics/radiology-workflow/README.md",
    "topics/therapy-analytics/README.md",
    "topics/decision-support/README.md",
    "topics/vendors/README.md",
    "topics/reimbursement/README.md",
    "topics/regulation/README.md",
    "topics/adoption-signals/README.md",
]

errors = []

for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f"Missing required file: {rel}")

pdfs = [p for p in ROOT.rglob("*.pdf") if ".git" not in p.parts]
if pdfs:
    errors.extend(f"Locally hosted PDF is not permitted by default: {p.relative_to(ROOT)}" for p in pdfs)

for brief in (ROOT / "briefs").rglob("*.md"):
    text = brief.read_text(encoding="utf-8")
    if "weekly-brief" in brief.name and "## Sources" not in text and "Status:** Planned" not in text:
        errors.append(f"Completed brief lacks Sources section: {brief.relative_to(ROOT)}")
    if "Status:** Planned" not in text:
        urls = re.findall(r"https://[^)\s]+", text)
        if not urls:
            errors.append(f"Completed brief has no HTTPS source URLs: {brief.relative_to(ROOT)}")

future = ROOT / "briefs/2026/2026-10-05-weekly-brief.md"
if future.exists() and "Status:** Planned" not in future.read_text(encoding="utf-8"):
    errors.append("Future 2026-10-05 brief must remain explicitly planned before publication date.")

if errors:
    print("VALIDATION_FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("VALIDATION_OK")
print(f"required_files={len(required)}")
print("local_pdfs=0")
