import pytest


@pytest.fixture(scope='package')
def init_browser():
    print("Open the browser")
    yield
    print("Browser close")


def test_m1(init_browser):
    print("Test case1")


def test_m2(init_browser):
    print("Test case2")


def test_m3(init_browser):
    print("Test case3")
