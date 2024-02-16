import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=ser)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
driver.implicitly_wait(30)

ele1 = driver.find_element(By.XPATH,"//span[text()='right click me']")
act = ActionChains(driver)
time.sleep(5)
act.context_click(ele1).perform()
time.sleep(5)