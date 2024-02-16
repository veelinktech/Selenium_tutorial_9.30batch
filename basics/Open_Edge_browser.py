import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

ser=Service(executable_path='D:\\Selenium Drivers\\edgedriver_win64\\msedgedriver.exe')
driver=webdriver.Edge(service=ser)
driver.get("http://www.instagram.com")
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.minimize_window()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.close()