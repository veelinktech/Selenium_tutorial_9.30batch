import pytest


@pytest.fixture(scope='function')
def init_browser():
    print("open the chrome browser")
    yield
    print("close the chrome browser")


def test_testcase1(init_browser):
    print('Test case1')


def test_testcase2(init_browser):
    print('Test case2')


def test_testcase3(init_browser):
    print('Test case3')
