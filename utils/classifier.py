import re


def is_in_sample(father, mother, proband):
    digit_pattern = re.compile(r"\d")
    return {
        "father": bool(digit_pattern.search(father)),
        "mother": bool(digit_pattern.search(mother)),
        "proband": bool(digit_pattern.search(proband)),
    }
