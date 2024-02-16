#click, isSelected, isEnabled, isDisplayed
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('http://www.fb.com')
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0_0')]").click()
male_radio_btn = driver.find_element(By.XPATH,"//input[@class='_8esa'][@value='2']")
f1 = male_radio_btn.is_enabled()
print("Male radio button is enable = ", f1)
f2 = male_radio_btn.is_displayed()
print("Male radio button is display = ", f2)
f3 = male_radio_btn.is_selected()
print("Male radio button is Select = ", f3)
male_radio_btn.click()
f4 = male_radio_btn.is_selected()
print("Male radio button is Select = ", f4)
time.sleep(5)