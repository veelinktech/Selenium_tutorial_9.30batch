from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def setup_module(module):
    global driver
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("http://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)


def teardown_module(module):
    driver.close()


def test_verifyTitle():
    actual_title = driver.title
    assert actual_title == "Facebook – log in or sign up"


def test_verifUrl():
    actual_url = driver.current_url
    assert actual_url == "https://www.facebook.com/"
