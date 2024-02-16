import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

ser = Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=ser)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[@data-testid='open-registration-form-button']").click()
driver.find_element(By.NAME,'firstname').send_keys('Raj')
act = ActionChains(driver)
(((act.send_keys(Keys.TAB).send_keys('K')
 .send_keys(Keys.TAB).send_keys('raj@gmail.com')
 .send_keys(Keys.TAB).send_keys('raj@gmail.com'))
 .send_keys(Keys.TAB)).send_keys('admin@123')
 .send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys('16').perform())
time.sleep(5)
