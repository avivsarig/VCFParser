import gzip
import os


from utils.get_file import file_from_s3
from utils.get_gene import gene_from_api
from utils.classifier import is_in_sample
from utils.wrap_file import lines_to_file

from parse_functions.columns import parse_column_names
from parse_functions.line import parse_data_line, unparse_data_line
from parse_functions.filter import is_filtered

FILE_PATH = os.getenv(
    "FILE_PATH", "s3://resources.genoox.com/homeAssingment/demo_vcf_multisample.vcf.gz"
)


def add_line(parsed_line, samples, deNovo):
    gene = gene_from_api(parsed_line)
    if gene:
        parsed_line["INFO"]["GENE"] = gene_from_api(parsed_line)

    classifier = is_in_sample(
        parsed_line["father"],
        parsed_line["mother"],
        parsed_line["proband"],
    )

    for key in classifier.keys():
        if deNovo and key == "proband":
            if (
                (not classifier["father"])
                and classifier["mother"]
                and classifier["proband"]
            ):
                samples[key].append(unparse_data_line(parsed_line))
                continue
        elif classifier[key]:
            samples[key].append(unparse_data_line(parsed_line))

    return samples


def process_vcf(
    limit: int, start: int = 0, end: int = -1, minDP: int = -1, deNovo: bool = False
):
    compressed_file = file_from_s3(FILE_PATH)
    if compressed_file is None:
        print("Failed to get the file from S3, exiting process.")
        return False

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
                    columns = parse_column_names(raw_columns[:-1])

            else:
                is_header_columned_parsed = True
                parsed_line = parse_data_line(line[:-1], columns)

                if is_filtered(parsed_line, start, end, minDP):
                    samples = add_line(parsed_line, samples, deNovo)

                    variant_procced += 1
                    if variant_procced == limit:
                        break

        for key in ["father", "mother", "proband"]:
            lines_to_file(key, header, raw_columns, samples[key])

        print(f"Done!")
