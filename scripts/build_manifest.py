"""Validate PRs and publish immutable, checksummed workflow sources."""
import argparse
import json
import re
import subprocess
from hashlib import sha256
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]

def build(ref, check_base=None):
    rows = []
    validator = Draft202012Validator(json.loads((ROOT / "schemas/workflow.json").read_text()))
    for folder in sorted((ROOT / "workflows").iterdir()):
        if not folder.is_dir():
            continue
        metadata = json.loads((folder / "publication.json").read_text())
        name, version = metadata["id"], metadata["version"]
        assert name == folder.name and re.fullmatch(r"[a-z0-9][a-z0-9._-]*", name), "Unique slug must match folder"
        assert re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][\w.-]+)?", version), "Use a semantic version"
        assert isinstance(metadata["description"], str) and metadata["description"].strip(), "Description required"
        path = folder / "workflow.json"
        document = json.loads(path.read_text())
        validator.validate(document)
        if check_base:
            old = subprocess.run(["git", "show", f"{check_base}:{path.relative_to(ROOT)}"], cwd=ROOT, capture_output=True, text=True)
            if old.returncode == 0 and json.loads(old.stdout) != document:
                previous = subprocess.check_output(["git", "show", f"{check_base}:{(folder / 'publication.json').relative_to(ROOT)}"], cwd=ROOT, text=True)
                assert json.loads(previous)["version"] != version, "Bump version when changing a workflow"
        rows.append({**metadata, "source": {"repository": "https://github.com/autostacgis/autostacgis-workflows", "ref": ref, "path": str(path.relative_to(ROOT)), "url": f"https://raw.githubusercontent.com/autostacgis/autostacgis-workflows/{ref}/{path.relative_to(ROOT)}", "sha256": sha256(path.read_bytes()).hexdigest()}})
    assert len({row["id"] for row in rows}) == len(rows), "Duplicate workflow ID"
    return {"format_version": 1, "workflows": rows}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref", default="main")
    parser.add_argument("--check-base")
    parser.add_argument("--output", default="workflows.json")
    args = parser.parse_args()
    Path(args.output).write_text(json.dumps(build(args.ref, args.check_base), indent=2) + "\n")
