#!/usr/bin/env python3
"""Utility to create downloadable bundles of the Clynico assets.

The script packages the `clynico_app` frontend (and optionally the CLI backend)
into a compressed archive so the bundle can be uploaded to external systems
without relying on `git clone` access. The generated archive preserves the
relative folder structure expected by the Firebase console or other hosting
solutions.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import zipfile
from typing import Iterable

EXCLUDE_PATTERNS = {
    "node_modules",
    ".git",
    "__pycache__",
    ".DS_Store",
}


def iter_files(base: Path) -> Iterable[Path]:
    """Yield all files under `base` skipping excluded directories."""
    for path in base.rglob("*"):
        if path.is_dir():
            if path.name in EXCLUDE_PATTERNS:
                # Skip the directory entirely by modifying the search.
                # `rglob` cannot be told to skip, so rely on the fact that
                # directories matching the pattern will be filtered out here
                # and their children will be ignored on subsequent iterations.
                continue
        elif path.is_file():
            parents = {parent.name for parent in path.parents}
            if parents & EXCLUDE_PATTERNS:
                continue
            yield path


def add_directory(zf: zipfile.ZipFile, directory: Path, prefix: str) -> None:
    """Add the contents of `directory` to the zip file using `prefix`."""
    base = directory.resolve()
    for file_path in iter_files(base):
        arcname = os.path.join(prefix, file_path.relative_to(base).as_posix())
        zf.write(file_path, arcname)


def create_bundle(output: Path, include_cli: bool, include_docs: bool) -> Path:
    project_root = Path(__file__).resolve().parents[1]
    app_dir = project_root / "clynico_app"
    if not app_dir.exists():
        raise SystemExit("The clynico_app directory was not found. Run the script from the repository root.")

    cli_dir = project_root / "patient_tracking"
    docs_dir = project_root / "docs"

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zf:
        add_directory(zf, app_dir, "clynico_app")
        if include_cli:
            if not cli_dir.exists():
                raise SystemExit("The patient_tracking package is missing; cannot include CLI bundle.")
            add_directory(zf, cli_dir, "patient_tracking")
        if include_docs and docs_dir.exists():
            add_directory(zf, docs_dir, "docs")

    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a distributable zip with the Clynico assets.")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("clynico_bundle.zip"),
        help="Destination zip file path (default: ./clynico_bundle.zip).",
    )
    parser.add_argument(
        "--include-cli",
        action="store_true",
        help="Include the Python patient tracking CLI in the bundle.",
    )
    parser.add_argument(
        "--include-docs",
        action="store_true",
        help="Include documentation files under docs/ in the archive.",
    )
    args = parser.parse_args()

    bundle_path = create_bundle(args.output, args.include_cli, args.include_docs)
    print(f"Bundle created at {bundle_path.resolve()}")


if __name__ == "__main__":
    main()
