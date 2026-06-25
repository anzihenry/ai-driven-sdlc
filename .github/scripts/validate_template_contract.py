#!/usr/bin/env python3

from __future__ import annotations

import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[2]
CONTRACT_PATH = ROOT / ".github" / "template-contract.json"
CONTRACT_DOC_PATH = ROOT / "doc" / "process" / "minimum-template-contract.md"


def load_contract() -> dict:
    try:
        return json.loads(CONTRACT_PATH.read_text())
    except FileNotFoundError:
        print(f"Missing contract manifest: {CONTRACT_PATH.relative_to(ROOT)}")
        sys.exit(1)


def ensure_paths_exist(paths: list[str], label: str) -> list[str]:
    missing = [path for path in paths if not (ROOT / path).exists()]
    if missing:
        print(f"Missing {label}:")
        for path in missing:
            print(f"  - {path}")
    return missing


def ensure_nonempty(paths: list[str], label: str) -> list[str]:
    empty = []
    for path in paths:
        target = ROOT / path
        if target.exists() and target.is_file() and target.stat().st_size == 0:
            empty.append(path)
    if empty:
        print(f"Empty {label}:")
        for path in empty:
            print(f"  - {path}")
    return empty


def ensure_forbidden_absent(paths: list[str]) -> list[str]:
    found = []
    for rel_path in ROOT.rglob("*"):
        if rel_path.name in paths:
            found.append(rel_path.relative_to(ROOT).as_posix())
    if found:
        print("Forbidden paths detected:")
        for path in found:
            print(f"  - {path}")
    return found


def extract_contract_doc_level(heading: str, marker: str) -> list[str]:
    text = CONTRACT_DOC_PATH.read_text()
    try:
        section = text.split(heading, 1)[1]
        section = section.split("### ", 1)[0]
        list_text = section.split(marker, 1)[1]
    except IndexError:
        print(f"Could not find contract documentation section for {heading.strip()}")
        return []

    paths = []
    for line in list_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- `") and stripped.endswith("`"):
            paths.append(stripped.removeprefix("- `").removesuffix("`"))
            continue
        if paths and stripped and not stripped.startswith("- "):
            break
    return paths


def ensure_contract_doc_matches_manifest(contract: dict) -> list[str]:
    expected_by_level = contract["adoption_levels"]
    documented_by_level = {
        "level_1": extract_contract_doc_level(
            "### Level 1: Minimum Supported Adoption",
            "Teams at this level should keep:",
        ),
        "level_2_additional": extract_contract_doc_level(
            "### Level 2: Recommended Team Adoption",
            "Teams at this level should keep everything in Level 1, plus:",
        ),
        "level_3_additional": extract_contract_doc_level(
            "### Level 3: Full Template Adoption",
            "Teams at this level should keep everything in Level 2, plus:",
        ),
    }

    mismatches = []
    for level, expected in expected_by_level.items():
        documented = documented_by_level[level]
        if documented == expected:
            continue
        missing_from_doc = [path for path in expected if path not in documented]
        extra_in_doc = [path for path in documented if path not in expected]
        if missing_from_doc:
            mismatches.append(f"{level} missing from docs: {missing_from_doc}")
        if extra_in_doc:
            mismatches.append(f"{level} extra in docs: {extra_in_doc}")
        if not missing_from_doc and not extra_in_doc:
            mismatches.append(f"{level} has the same paths but a different order")

    if mismatches:
        print("Contract documentation and machine-readable manifest are out of sync:")
        for mismatch in mismatches:
            print(f"  - {mismatch}")
    return mismatches


def ensure_level_files_are_classified(contract: dict) -> list[str]:
    level_1_allowed = set(contract["repository_required_files"]) | set(
        contract["core_contract_files"]
    )
    level_2_allowed = set(contract["recommended_contract_files"])
    level_3_allowed = set(contract["optional_extension_files"])
    checks = {
        "level_1": (contract["adoption_levels"]["level_1"], level_1_allowed),
        "level_2_additional": (
            contract["adoption_levels"]["level_2_additional"],
            level_2_allowed,
        ),
        "level_3_additional": (
            contract["adoption_levels"]["level_3_additional"],
            level_3_allowed,
        ),
    }

    unclassified = []
    for level, (paths, allowed) in checks.items():
        for path in paths:
            if path not in allowed:
                unclassified.append(f"{level}: {path}")
    if unclassified:
        print("Adoption-level files are missing from their validation category:")
        for path in unclassified:
            print(f"  - {path}")
    return unclassified


def is_local_path_reference(value: str) -> bool:
    if " " in value:
        return False
    if value.startswith("http://") or value.startswith("https://"):
        return False
    if value.startswith("./"):
        return True
    if "/" in value:
        return True
    return value.startswith(".github/")


def extract_inline_code_values(text: str) -> list[str]:
    text_without_fences = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    return re.findall(r"`([^`\n]+)`", text_without_fences)


def ensure_example_references_exist(paths: list[str]) -> list[str]:
    missing = []
    for path in paths:
        doc_path = ROOT / path
        if not doc_path.exists():
            missing.append(f"{path}: example document is missing")
            continue
        for value in extract_inline_code_values(doc_path.read_text()):
            if not is_local_path_reference(value):
                continue
            target = ROOT / value.removeprefix("./")
            if not target.exists():
                missing.append(f"{path}: `{value}` does not exist")
    if missing:
        print("Example documentation references missing local paths:")
        for item in missing:
            print(f"  - {item}")
    return missing


def main() -> int:
    contract = load_contract()

    missing = []
    empty = []
    contract_mismatches = []
    unclassified = []
    missing_example_refs = []

    missing += ensure_paths_exist(
        contract["repository_required_files"], "repository-required files"
    )
    missing += ensure_paths_exist(
        contract["core_contract_files"], "core contract files"
    )

    empty += ensure_nonempty(
        contract["required_nonempty_files"], "required non-empty files"
    )
    empty += ensure_nonempty(
        contract["optional_nonempty_files"], "optional non-empty files that are present"
    )

    forbidden = ensure_forbidden_absent(contract["forbidden_paths"])
    contract_mismatches = ensure_contract_doc_matches_manifest(contract)
    unclassified = ensure_level_files_are_classified(contract)
    missing_example_refs = ensure_example_references_exist(contract["example_docs"])

    if (
        missing
        or empty
        or forbidden
        or contract_mismatches
        or unclassified
        or missing_example_refs
    ):
        return 1

    print("Template contract validation passed.")
    print(
        "Validated core contract files, adoption-level sync, example references, and present-if-kept optional surfaces."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
