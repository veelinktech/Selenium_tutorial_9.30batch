def test_verify_m6():
    str = 'python'
    assert str.upper() == "PYTHON"


def test_verify_m7():
    a, b, c = 5, 15, 25
    assert a + b == c - b

def test_group_m8():
    s = "I Am A Automation Tester"
    assert s.title() == s