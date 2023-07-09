from ..parse_functions.filter import is_filtered

def test_is_filtered():
    line = {
        "POS": "100",
        "INFO": {
            "DP": "50"
        }
    }
    assert is_filtered(line, 50, 150, 10) == True
    assert is_filtered(line, 200, 300, 10) == False
    assert is_filtered(line, 50, 150, 60) == False
