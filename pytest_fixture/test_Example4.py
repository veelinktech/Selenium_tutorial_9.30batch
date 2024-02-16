import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pytest_fixture.conftest import init_chrome_browser


@pytest.mark.parametrize("username, password",
                         [
                             ('Admin', 'admin123'),
                             ('admin', 'admin123'),
                             ('Admin', 'admin123'),
                             ('admin', 'admin123'),
                             ('Admin', 'admin123')
                         ])
def test_verifyLogin(username, password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[normalize-space(text()='Login')]").click()
    driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Logout").click()
    time.sleep(5)
    driver.close()
