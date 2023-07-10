import os
import glob
import json
import gzip
import typer

from process import process_vcf

app = typer.Typer(
    help="A VCF file parser and filter. It handles compressed VCF files from Amazon S3, parses and filters them, then outputs the results into separate files for father, mother, and proband."
)


@app.command()
def process(
    limit: int = typer.Option(..., help="The maximum number of variants to process."),
    start: int = typer.Option(0, help="The start position for filtering."),
    end: int = typer.Option(-1, help="The end position for filtering."),
    minDP: int = typer.Option(-1, help="The minimum depth to filter by."),
    deNovo: bool = typer.Option(False, help="Whether to include de novo mutations."),
):
    """
    Download, parse, filter and output a VCF file.

    This command takes a compressed VCF file from S3, parses it, applies filters based on given arguments, and outputs the results into separate files for father, mother, and proband.
    """
    if limit >= 10:
        print("Limit must be smaller than 10")
        return False
    return process_vcf(limit, start, end, minDP, deNovo)


@app.command()
def clear_cache():
    """
    Clears the Gene Cache.

    Use this command to reset the contents of the gene cache. This action cannot be undone.
    """
    confirmation = input(
        f"Are you sure you want to reset the contents of the Gene Cache? This cannot be undone.\nEnter (yes/no): "
    )
    if confirmation.lower() == "yes":
        with open("gene_cache.json", "w") as f:
            json.dump({}, f)
        print(f"Contents of the Gene Cache have been reset.")
    else:
        print("Operation cancelled.")


@app.command()
def clear_output():
    """
    Clears the output folder.

    Use this command to reset the contents of the output folder. This action cannot be undone.
    """
    confirmation = input(
        f"Are you sure you want to reset the contents of the output folder? This cannot be undone.\nEnter (yes/no): "
    )
    if confirmation.lower() == "yes":
        files = glob.glob("./output/*")
        for f in files:
            os.remove(f)
        print(f"Contents of the output folder have been reset.")
    else:
        print("Operation cancelled.")


if __name__ == "__main__":
    app()
