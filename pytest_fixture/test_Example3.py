import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.mark.usefixtures("init_all_browser")
class TestBase:
    pass


class Test_chrome(TestBase):

    def test_verify_title(self):
        self.driver.get("http://www.fb.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        actual_title = self.driver.title
        assert actual_title == "Facebook – log in or sign up"

    def test_verify_url(self):
        self.driver.get("http://www.fb.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        actual_url = self.driver.current_url
        assert actual_url == "https://www.facebook.com/"
