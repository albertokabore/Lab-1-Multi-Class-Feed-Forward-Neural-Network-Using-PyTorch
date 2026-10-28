"""Execute every lab cell in a fresh kernel and save actual outputs."""

from pathlib import Path

import nbformat
from nbclient import NotebookClient


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "Lab1_FFNN_BoW_AG_News.ipynb"


def main():
    notebook = nbformat.read(NOTEBOOK, as_version=4)
    nbformat.validate(notebook)

    def announce(cell, cell_index, **kwargs):
        if cell.cell_type == "code":
            first_line = cell.source.splitlines()[0] if cell.source else ""
            print(f"Running cell {cell_index + 1}: {first_line}", flush=True)

    client = NotebookClient(
        notebook,
        timeout=1800,
        kernel_name="python3",
        resources={"metadata": {"path": str(ROOT)}},
        on_cell_start=announce,
    )
    try:
        client.execute()
    finally:
        nbformat.write(notebook, NOTEBOOK)
    print("Completed all cells and saved notebook outputs.", flush=True)


if __name__ == "__main__":
    main()
