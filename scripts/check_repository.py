"""Static notebook validation; reports missing inputs without claiming replication."""
import ast
import argparse
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--require-data", action="store_true")
args = parser.parse_args()
for path in sorted((root / "notebooks").glob("*.ipynb")):
    notebook = json.loads(path.read_text())
    assert notebook["nbformat"] == 4
    assert isinstance(notebook["cells"], list)
    for index, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] == "code":
            ast.parse("".join(cell["source"]), filename=f"{path.name}:cell-{index}")
    print(f"PASS structure and syntax: {path.name}")
required = ["events_monthly_northern_ireland.csv", "kg_theme_counts_northern_ireland.csv",
            "kg_theme_counts_northern_ireland_STRICT.csv", "psni_monthly.csv"]
missing = [name for name in required if not (root / "data" / name).exists()]
for name in missing:
    print(f"MISSING INPUT: {name}")
print("Static validation only; statistical results have not been reproduced.")
if args.require_data and missing:
    raise SystemExit(1)
