#!/usr/bin/env python3
"""Validate the ECE Formula Vault data and its browser bundle."""
from __future__ import annotations
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data.json"
BUNDLE_FILE = ROOT / "assets" / "js" / "catalog.js"


def validate() -> int:
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot load data.json: {exc}")
        return 1

    errors: list[str] = []
    subjects = data.get("subjects")
    if not isinstance(subjects, list) or not subjects:
        errors.append("subjects must be a non-empty array")
        subjects = []

    ids: set[str] = set()
    formula_count = 0
    unit_count = 0
    for subject_index, subject in enumerate(subjects):
        label = subject.get("code") or f"subject index {subject_index}"
        for key in ("id", "code", "name", "year", "semester", "category", "units"):
            if key not in subject:
                errors.append(f"{label}: missing subject field {key}")
        subject_id = subject.get("id")
        if not isinstance(subject_id, str) or not subject_id.strip():
            errors.append(f"{label}: invalid id")
        elif subject_id in ids:
            errors.append(f"{label}: duplicate id {subject_id}")
        else:
            ids.add(subject_id)
        if subject.get("year") not in (1, 2, 3, 4):
            errors.append(f"{label}: year must be 1–4")
        units = subject.get("units")
        if not isinstance(units, list) or len(units) != 5:
            errors.append(f"{label}: expected five unit records")
            continue
        for unit_index, unit in enumerate(units):
            unit_count += 1
            unit_label = f"{label} / Unit {unit_index + 1}"
            if not unit.get("title"):
                errors.append(f"{unit_label}: missing title")
            if not isinstance(unit.get("formulas"), list):
                errors.append(f"{unit_label}: formulas must be an array")
                continue
            for formula_index, formula in enumerate(unit["formulas"]):
                formula_count += 1
                formula_label = f"{unit_label} / Formula {formula_index + 1}"
                if not isinstance(formula.get("name"), str) or not formula["name"].strip():
                    errors.append(f"{formula_label}: missing formula name")
                expression = formula.get("formula")
                if not isinstance(expression, str) or not expression.strip():
                    errors.append(f"{formula_label}: missing formula expression")
                elif any(word in expression.lower() for word in ("todo", "tbd", "undefined", "placeholder")):
                    errors.append(f"{formula_label}: placeholder text in expression")

    try:
        bundle = BUNDLE_FILE.read_text(encoding="utf-8")
        prefix = "window.ECE_DATA = "
        if not bundle.startswith(prefix) or not bundle.rstrip().endswith(";"):
            errors.append("catalog.js does not have the expected window.ECE_DATA wrapper")
        else:
            bundled_data = json.loads(bundle[len(prefix):].strip().rstrip(";").strip())
            if bundled_data != data:
                errors.append("catalog.js and data.json are out of sync; rerun python build_data.py")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot validate catalog.js: {exc}")

    if errors:
        print(f"FAIL: {len(errors)} issue(s)")
        for error in errors:
            print(f" - {error}")
        return 1

    print("PASS: catalogue structure and browser bundle are valid")
    print(f"      {len(subjects)} subjects · {unit_count} units · {formula_count} formula cards")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
