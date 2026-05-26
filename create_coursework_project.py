#!/usr/bin/env python3
"""
Initialize a new UK master coursework project from Master_Coursework_OS templates.
Stdlib only. Run: python create_coursework_project.py
"""
from __future__ import annotations

import re
import shutil
from datetime import datetime
from pathlib import Path

OS_ROOT = Path(__file__).resolve().parent
TEMPLATE_ROOT = OS_ROOT / "05_Project_Template"
TEMPLATES = OS_ROOT / "03_Templates"
INTAKE_MASTER = OS_ROOT / "01_Intake_Form" / "Assignment_Intake_Form.md"

MODULE0_MASTER = OS_ROOT / "02_SOP" / "Module0_AI_Policy_Gate.md"

COPY_FILES = [
    (TEMPLATES / "task_plan.md", "task_plan.md"),
    (TEMPLATES / "core_argument_paragraph.md", "02_Notes/core_argument_paragraph.md"),
    (TEMPLATES / "reading_notes_template.md", "02_Notes/reading_notes_template.md"),
    (TEMPLATES / "rubric_mapping_table.md", "rubric_mapping_table.md"),
    (TEMPLATES / "draft_structure.md", "04_Draft/draft_structure.md"),
    (TEMPLATES / "final_submission_checklist.md", "06_Final/final_submission_checklist.md"),
    (TEMPLATES / "literature_table.md", "03_Literature/literature_table.md"),
    (TEMPLATES / "literature_table.csv", "03_Literature/literature_table.csv"),
    (TEMPLATES / "reference_verification_table.csv", "03_Literature/reference_verification_table.csv"),
    (TEMPLATES / "ai_log.md", "05_AI_Log/ai_log.md"),
    (TEMPLATES / "ai_log.csv", "05_AI_Log/ai_log.csv"),
    (TEMPLATES / "ai_declaration_template.md", "06_Final/ai_declaration.md"),
]


def slug(s: str) -> str:
    s = s.strip().replace(" ", "_")
    return re.sub(r"[^\w\-]", "", s, flags=re.UNICODE)[:40] or "Assignment"


def prompt(msg: str, default: str = "") -> str:
    line = input(f"{msg}" + (f" [{default}]" : "") + ": ").strip()
    return line or default


def main() -> None:
    print("Master Coursework OS — New Project\n")
    module = prompt("Module name/code", "MODULE")
    assignment = prompt("Assignment name", "Essay1")
    deadline = prompt("Deadline (YYYY-MM-DD)", "")
    target = prompt("Target grade (Pass/Merit/Distinction)", "Merit")
    hours = prompt("Estimated hours", "20")

    folder_name = f"{datetime.now().year}_{slug(module)}_{slug(assignment)}"
    parent = prompt("Parent folder (empty = current directory)", "")
    base = Path(parent).expanduser().resolve() if parent else Path.cwd()
    dest = base / folder_name

    if dest.exists():
        print(f"Error: {dest} already exists.")
        raise SystemExit(1)

    print(f"\nCreating: {dest}\n")

    # Copy template tree
    shutil.copytree(TEMPLATE_ROOT, dest)

    # Copy intake form
    brief = dest / "01_Brief"
    brief.mkdir(parents=True, exist_ok=True)
    shutil.copy2(INTAKE_MASTER, brief / "Assignment_Intake_Form.md")
    if MODULE0_MASTER.exists():
        shutil.copy2(MODULE0_MASTER, brief / "Module0_AI_Policy_Gate.md")

    # Patch intake header
    intake = (brief / "Assignment_Intake_Form.md").read_text(encoding="utf-8")
    intake = intake.replace("| Module name | |", f"| Module name | {module} |")
    intake = intake.replace("| Assignment title | |", f"| Assignment title | {assignment} |")
    if deadline:
        intake = intake.replace("| Deadline (date + time + timezone) | |", f"| Deadline | {deadline} |")
    intake = intake.replace("| Target grade |", f"| Target grade | {target} |")
    intake = intake.replace("| Available time (hours) | |", f"| Available time (hours) | {hours} |")
    (brief / "Assignment_Intake_Form.md").write_text(intake, encoding="utf-8")

    # Cursor rules (so opening only the assignment folder still has SOP 2.0 rules)
    rules_src = OS_ROOT / ".cursor" / "rules"
    if rules_src.is_dir():
        rules_dest = dest / ".cursor" / "rules"
        rules_dest.mkdir(parents=True, exist_ok=True)
        for rule_file in rules_src.glob("*.mdc"):
            shutil.copy2(rule_file, rules_dest / rule_file.name)

    # Copy workspace templates
    for src, rel in COPY_FILES:
        if src.exists():
            target_path = dest / rel
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, target_path)

    # README
    readme = dest / "project_readme.md"
    text = readme.read_text(encoding="utf-8")
    text = text.replace("[ModuleCode]", module).replace("[AssignmentName]", assignment)
    if deadline:
        text = text.replace("**Deadline**:", f"**Deadline**: {deadline}")
    readme.write_text(text, encoding="utf-8")

    print("Done.\nNext steps:")
    print(f"  1. cd {dest}")
    print("  2. Complete 01_Brief/Module0_AI_Policy_Gate.md (UK: required)")
    print("  3. Fill 01_Brief/Assignment_Intake_Form.md")
    print("  4. Cursor: 04_Prompt_Library/08_cursor_project_bootstrap_prompt.md")
    print("  5. ChatGPT: 00_chatgpt_session_opener.md + Intake")
    print(f"\nSee: {OS_ROOT / 'Next_Assignment_Quickstart.md'}")
    print(f"Main SOP: {OS_ROOT / '02_SOP' / 'Master_Coursework_SOP_2.0.md'}")
    print(f"Bib check: py -3 {OS_ROOT / 'tools' / 'verify_bib_keys.py'} <draft> 03_Literature/refs.bib")


if __name__ == "__main__":
    main()
