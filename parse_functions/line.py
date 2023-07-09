def parse_data_line(line, columns):
    parsed_line_list = line.split("\t")
    parsed_line = dict(zip(columns, parsed_line_list))

    info = {}
    for item in parsed_line["INFO"].split(";"):
        try:
            key, value = item.split("=")
            info[key] = value
        
        except ValueError as e:
            print(f"Error parsing INFO field: {e}. Item: {item}")

    parsed_line["INFO"] = info

    return parsed_line


def unparse_data_line(parsed_line):
    if type(parsed_line['INFO']) == dict:
        unparsed_info = []
        for key, value in parsed_line["INFO"].items():
            unparsed_instance = f"{key}={value}"
            unparsed_info.append(unparsed_instance)
        parsed_line["INFO"] = ";".join(unparsed_info)

    return "\t".join(parsed_line.values())
