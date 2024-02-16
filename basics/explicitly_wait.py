import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

Ser = Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service = Ser)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0_0')]").click()
wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.NAME,'firstname'))).send_keys('RAM')
driver.find_element(By.NAME,'lastname').send_keys('K')
driver.find_element(By.NAME,'reg_email__').send_keys('9775435260')
time.sleep(5)