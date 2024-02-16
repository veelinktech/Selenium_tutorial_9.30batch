import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

ser=Service(executable_path='D:\\Selenium Drivers\\geckodriver-v0.33.0-win64\\geckodriver.exe')
driver=webdriver.Firefox(service=ser)
driver.get("http://www.flipkart.com")
driver.minimize_window()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.close()