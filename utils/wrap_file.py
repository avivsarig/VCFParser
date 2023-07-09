def lines_to_file(sample_name, header, raw_columns, current_sample):
    file_name = f"{sample_name}_filtered.vcf"
    joint_header = "".join(header)
    joint_data = "\n".join(current_sample)
    file_content = "".join([joint_header, raw_columns, joint_data])

    try:
        with open(f"output/{file_name}", "w") as f:
            f.write(file_content)

    except IOError as e:
        print(f"Error writing to file {file_name}: {e}")
        return False


    print(f"{file_name} created successfully")
