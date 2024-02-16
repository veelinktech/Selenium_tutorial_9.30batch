import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service = s)
driver.get('http://www.fb.com')
driver.maximize_window()
driver.implicitly_wait(30)
ele = driver.find_element(By.ID,'email')

attr1 = ele.get_attribute('data-testid')
print(attr1)

attr2 = ele.get_attribute('placeholder')
print(attr2)

attr3 = ele.get_attribute('name')
print(attr3)

ele.send_keys('Ram')
time.sleep(5)

attr4 = ele.get_attribute('value')
print(attr4)

fs = ele.value_of_css_property('font-size')
print(fs)

wd = ele.value_of_css_property('width')
print(wd)

hg = ele.value_of_css_property('height')
print(hg)

