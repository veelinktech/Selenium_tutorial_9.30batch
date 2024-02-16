import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.get('http://www.fb.com')
driver.maximize_window()
#id locator
driver.find_element(By.ID,"email").send_keys('Raj@gmail.com')
time.sleep(5)
#name locator
driver.find_element(By.NAME,'pass').send_keys('selenium123')
time.sleep(5)
#className locator
actual_text=driver.find_element(By.CLASS_NAME,'_8eso').text
print(actual_text)
time.sleep(5)
#Link_text locator
actual_fpass = driver.find_element(By.LINK_TEXT,'Forgotten password?').text
print(actual_fpass)

#partial link text locator
actual_fpass1=driver.find_element(By.PARTIAL_LINK_TEXT,'ten').text
print(actual_fpass1)

