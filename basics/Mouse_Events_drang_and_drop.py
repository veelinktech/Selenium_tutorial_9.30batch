import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe'))
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
ele1 = driver.find_element(By.ID,"draggable")
ele2 = driver.find_element(By.ID,"droppable")
act = ActionChains(driver)
act.drag_and_drop(ele1,ele2).perform()
time.sleep(10)