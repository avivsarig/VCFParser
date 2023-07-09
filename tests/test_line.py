from ..parse_functions.line import parse_data_line, unparse_data_line

def test_parse_and_unparse_data_line():
    columns = ["CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT", "father", "mother", "proband"]
    line = "chr1\t12345\trs12345\tA\tG\t30\tPASS\tDP=100;AF=0.5\tGT:GQ:DP\t0/1:60:50\t0/0:60:50\t0/1:60:50"
    parsed_line = parse_data_line(line, columns)
    assert parsed_line["CHROM"] == "chr1"
    assert parsed_line["INFO"]["DP"] == "100"
    unparsed_line = unparse_data_line(parsed_line)
    assert unparsed_line == line
