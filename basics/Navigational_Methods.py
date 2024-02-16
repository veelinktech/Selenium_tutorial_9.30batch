import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

se=Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(service=se)
driver.get('http://www.fb.com')
driver.maximize_window()
time.sleep(5)
driver.get('http://www.google.com')
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.close()

#