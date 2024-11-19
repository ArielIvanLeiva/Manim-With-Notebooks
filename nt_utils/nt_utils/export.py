import sys
import argparse
import nbformat

def main():
    args = parse_args()
    
    export_cells(args.notebook_file, args.output_file, args.tags, args.ignored_tags)

def parse_args():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Example script with flags.")

    parser.add_argument(
        "notebook_file",
        type=str,
        help="The name of the notebook file to process"
    )

    parser.add_argument(
        "-o", "--output-file", 
        type=str,
        default="exported_cells.py",
        help="Specify output file for the exported cells"
    )
    
    parser.add_argument(
        "-t", "--tags",
        type=str,
        nargs='+',
        default=[],
        help="Tags of cells to be exported. If empty, the script will try to export all code cells."
    )
    
    parser.add_argument(
        "-i", "--ignored-tags",
        type=str,
        nargs='+',
        default=[],
        help="Tags for cells to be ignored."
    )
    
    args = parser.parse_args()
    
    return args

def export_cells(notebook_file, output_file, tags, ignored_tags):

    # Load the notebook
    with open(notebook_file, "r") as f:
        notebook = nbformat.read(f, as_version=4)

    # Filter cells witch have a tag from tags
    selected_cells = [
        cell.source
        for cell in notebook.cells
        if (
            (any(tag in cell.metadata.get("tags", []) for tag in tags) or tags == [])
            and
            (all(tag not in cell.metadata.get("tags", []) for tag in ignored_tags))
            and
            cell.cell_type == "code"
        )
    ]

    # Write the filtered cells to a Python script
    with open(output_file, "w") as f:
        for cell in selected_cells:
            f.write(cell + "\n\n")

    print(f"Exported cells saved to {output_file}.")

if (__name__ == "__main__"):
    main()
