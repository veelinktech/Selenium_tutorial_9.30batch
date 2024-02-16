import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.rediff.com/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get_screenshot_as_file("C:\\Users\\pc\\Desktop\\Demo\\SS1.png")
driver.save_screenshot("C:\\Users\\pc\\Desktop\\Demo\\SS2.jpg")
time.sleep(10)
driver.close()