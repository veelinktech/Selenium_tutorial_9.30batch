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
ele2 = driver.find_element(By.XPATH,"//button[text()='Double-Click Me To See Alert']")
act = ActionChains(driver)
time.sleep(5)
act.double_click(ele2).perform()
time.sleep(5)
alt = driver.switch_to.alert
alt.accept()
time.sleep(5)