from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def setup_module(module):
    global driver
    s = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=s)
    driver.get("http://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)


def teardown_module(module):
    driver.close()


def test_verifyTitle():
    actual_title = driver.title
    assert actual_title == "Facebook – log in or sign up"


def test_verifyUrl():
    actual_url = driver.current_url
    assert actual_url == "https://www.facebook.com/"


def test_verifyLogin_btn():
    actual_login_text = driver.find_element(By.NAME, "login").text
    assert actual_login_text == "Log in"
