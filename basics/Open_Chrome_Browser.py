import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser=Service(executable_path="D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=ser)
driver.get('http://www.fb.com')
driver.maximize_window()
time.sleep(5)
driver.minimize_window()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.close()