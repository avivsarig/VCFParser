import os
import glob
import json
import gzip
import typer

from utils.config import FILE_PATH

from utils.get_file import file_from_s3
from utils.get_gene import gene_from_api
from utils.wrap_file import lines_to_file
from utils.classifier import is_in_sample

from parse_functions.columns import parse_columns
from parse_functions.line import parse_data_line, unparse_data_line
from parse_functions.filter import is_filtered

app = typer.Typer()


@app.command()
def filter(limit: int, start: int = 0, end: int = -1, minDP: int = -1, deNovo: bool = False):
    if limit >= 10:
        print("Limit must be smaller than 10")
        return False

    compressed_file = file_from_s3(FILE_PATH)
    header = []
    is_header_columned_parsed = False

    variant_procced = 0
    samples = {"father": [], "mother": [], "proband": []}

    with gzip.open(compressed_file, "rt") as compressed_file:
        for line in compressed_file:
            if not is_header_columned_parsed and line.startswith("#"):
                if line.startswith("##"):
                    header.append(line)
                else:
                    raw_columns = line
                    columns = parse_columns(raw_columns[:-1])

            else:
                is_header_columned_parsed = True
                parsed_line = parse_data_line(line[:-1], columns)

                if is_filtered(parsed_line, start, end, minDP):
                    gene = gene_from_api(parsed_line)
                    if gene:
                        parsed_line["INFO"]["GENE"] = gene_from_api(parsed_line)

                    classifier = is_in_sample(
                        parsed_line["father"],
                        parsed_line["mother"],
                        parsed_line["proband"],
                    )


                        

                    for key in classifier.keys():
                        if deNovo and key == 'proband':
                            if classifier['father'] == False and classifier['mother'] == False and classifier['proband'] == True:
                                samples[key].append(unparse_data_line(parsed_line))
                                continue
                        elif classifier[key]:
                            samples[key].append(unparse_data_line(parsed_line))

                    variant_procced += 1
                    if variant_procced == limit:
                        break

        for key in classifier.keys():
            lines_to_file(key, header, raw_columns, samples[key])

        print(f"Done!")


@app.command()
def clear_cache():
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
