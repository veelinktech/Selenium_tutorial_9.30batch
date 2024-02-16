import pytest


@pytest.mark.Smoke
def test_validateTitle():
    assert 5 + 5 == 10


@pytest.mark.Regression
def test_validateM1():
    assert 5 + 10 >= 15


@pytest.mark.Sanity
def test_validateM2():
    assert 'Python' == 'python'
