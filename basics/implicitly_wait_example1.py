import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# driver can wait for a particular time to load all the webelements in to the webpage.
Ser = Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service = Ser)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0_0')]").click()
driver.find_element(By.NAME,'firstname').send_keys('Ram')
driver.find_element(By.NAME,'lastname').send_keys('K')
driver.find_element(By.NAME,'reg_email__').send_keys('9775435260')
time.sleep(5)