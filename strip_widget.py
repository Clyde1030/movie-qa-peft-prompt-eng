"""
This script removes the "widgets" metadata from Jupyter notebooks.

Usage:
# single file
uv run strip_widget.py base_and_peft/266_Final_Project_WIP_Cassie.ipynb

# multiple files
uv run strip_widget.py base_and_peft/*.ipynb prompt_styles/*.ipynb
"""
# /// script
# requires-python = ">=3.12"
# dependencies = ["nbformat>=5.10.4"]
# ///
import argparse
import nbformat


def strip_widget_metadata(path: str) -> None:
    with open(path, "r") as f:
        nb = nbformat.read(f, as_version=4)

    if "widgets" in nb.metadata:
        del nb.metadata["widgets"]
        with open(path, "w") as f:
            nbformat.write(nb, f)
        print(f"Removed widget metadata from {path}")
    else:
        print(f"No widget metadata found in {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove widget metadata from Jupyter notebooks")
    parser.add_argument("notebooks", nargs="+", help="Path(s) to .ipynb file(s)")
    args = parser.parse_args()

    for notebook in args.notebooks:
        strip_widget_metadata(notebook)
