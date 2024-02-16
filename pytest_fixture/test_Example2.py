import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_verifyCreatenewaccount_text(init_browser):
    driver=driver=init_browser
    expected_text = "Create new account"
    actual_text = driver.find_element(By.PARTIAL_LINK_TEXT, "new account").text
    assert actual_text == expected_text


def test_Signup_heading(init_browser):
    driver=init_browser
    expected_text = "Sign Up"
    driver.find_element(By.PARTIAL_LINK_TEXT,"new account").click()
    actual_text = driver.find_element(By.XPATH, "//div[text()='Sign Up']").text
    assert actual_text == expected_text
