import pytest


@pytest.mark.smoke
def test_verify_m1():
    str = 'python'
    assert str.upper() == "PYTHON"


@pytest.mark.regression
def test_verify_m2():
    a, b, c = 5, 15, 25
    assert a + b == c - b


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.sanity
def test_verify_m3():
    s = "I Am A Automation Tester"
    assert s.title() == s


@pytest.mark.regression
def test_group_m4():
    s = "I Am A Automation Tester"
    assert s.title() == s


@pytest.mark.regression
def test_group_m5():
    s = "I Am A Automation Tester"
    assert s.title() == s


@pytest.mark.smoke
def test_validate_m6():
    a, b = 10, 25
    c = a + b
    assert c == 35
