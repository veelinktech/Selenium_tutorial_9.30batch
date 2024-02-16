import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.NAME,'proceed').click()
alt = driver.switch_to.alert
actual_popup_text= alt.text
print(actual_popup_text)
time.sleep(5)
alt.accept()
time.sleep(10)