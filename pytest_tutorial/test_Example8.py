import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope='module')
def setup_module():
    print("======setup======")
    global driver
    s = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=s)
    driver.get("http://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield
    print("=====teardown=====")
    driver.close()


def test_verifyTitle(setup_module):
    actual_title = driver.title
    assert actual_title == "Facebook – log in or sign up"


def test_verifyUrl(setup_module):
    actual_url = driver.current_url
    assert actual_url == "https://www.facebook.com/"


def test_verifyLogin_btn(setup_module):
    actual_login_text = driver.find_element(By.NAME, "login").text
    assert actual_login_text == "Log in"
