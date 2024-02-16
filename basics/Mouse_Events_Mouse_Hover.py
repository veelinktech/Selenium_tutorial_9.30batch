import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Mouse Hover, right click, double click , drag and drop

driver = webdriver.Chrome(service=Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe'))
driver.get("https://www.naukri.com/")
driver.maximize_window()
driver.implicitly_wait(30)
ele1 = driver.find_element(By.XPATH, "//div[text()='Companies']")
act = ActionChains(driver)
act.move_to_element(ele1).perform()
time.sleep(10)
driver.find_element(By.XPATH, "//a[@title='IT companies']").click()
time.sleep(10)
