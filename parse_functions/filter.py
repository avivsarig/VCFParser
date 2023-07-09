def is_filtered(parsed_line, start, end, minDP):
    if int(parsed_line["POS"]) < start:
        return False

    if (end != -1) and (int(parsed_line["POS"]) > end):
        return False

    if int(parsed_line["INFO"]["DP"]) < minDP:
        return False

    return True
