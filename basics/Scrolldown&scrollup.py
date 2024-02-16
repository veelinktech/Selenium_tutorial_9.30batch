import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("http://www.rediff.com")
driver.maximize_window()
driver.implicitly_wait(30)
#print(driver.execute_script("document.documentElement.scrollHeight"))
driver.execute_script("window.scrollBy(0,2000)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,-2000)")
time.sleep(5)