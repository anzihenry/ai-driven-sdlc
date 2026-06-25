#!/usr/bin/env python3

from __future__ import annotations

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
CONTRACT_PATH = ROOT / ".github" / "template-contract.json"


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


def main() -> int:
    contract = load_contract()

    missing = []
    empty = []

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

    if missing or empty or forbidden:
        return 1

    print("Template contract validation passed.")
    print(
        "Validated core contract files and treated recommended/optional surfaces as present-if-kept."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
