import pytest


def test_m1():
    print('Test case1')


@pytest.mark.skip
def test_m2():
    print('Test case2')


@pytest.mark.xfail
def test_m3():
    print('Test case3')


@pytest.mark.skip
def test_m4():
    print('Test case4')


@pytest.mark.skipif
def test_m5():
    print('Test case5')
