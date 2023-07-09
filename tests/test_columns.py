from ..parse_functions.columns import parse_columns

def test_parse_columns():
    raw_columns = "#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tfather\tmother\tproband"
    result = parse_columns(raw_columns)
    assert result == ["CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT", "father", "mother", "proband"]
