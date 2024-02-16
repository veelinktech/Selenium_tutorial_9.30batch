import pytest

@pytest.mark.Smoke
@pytest.mark.Sanity
@pytest.mark.Regression
def test_verifyTitle():
    str = 'python'
    assert str.upper() == "PYTHON"

@pytest.mark.Sanity
def test_verifyUrl():
    a, b, c = 5, 15, 25
    assert a + b == c - b

@pytest.mark.Regression
@pytest.mark.Sanity
def test_verifyString():
    s = "I Am A Automation Tester"
    assert s.title() == s

@pytest.mark.Smoke
def test_validateString():
    s = "I am a automation tester"
    assert s.capitalize() == s

@pytest.mark.Regression
def test_groupString():
    assert 100 >= 100

@pytest.mark.Sanity
@pytest.mark.Regression
def test_groupString1():
    assert 25 < 20
