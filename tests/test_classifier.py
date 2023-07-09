from ..utils.classifier import is_in_sample

def test_is_in_sample():
    assert is_in_sample("0/1", "0/0", "0/1") == {"father": True, "mother": False, "proband": True}
    assert is_in_sample(".", ".", ".") == {"father": False, "mother": False, "proband": False}
