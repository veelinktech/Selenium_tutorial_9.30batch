import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_FB():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("http://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    actual_title = driver.title
    assert actual_title == "Facebook – log in or sign up"
    driver.close()


def test_Google():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("http://www.google.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    actual_title = driver.title
    assert actual_title == "Google"
    driver.close()


def test_insta():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.instagram.com/")
    driver.maximize_window()
    driver.implicitly_wait(30)
    actual_title = driver.title
    assert actual_title == "Instagram"
    driver.close()


def test_twitter():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://twitter.com/")
    driver.maximize_window()
    driver.implicitly_wait(30)
    actual_title = driver.title
    assert actual_title == "X. It’s what’s happening / X"
    driver.close()
