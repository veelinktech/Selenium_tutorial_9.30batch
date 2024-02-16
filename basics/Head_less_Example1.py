import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service

opt = Options()
opt.add_argument("--headless")
S = Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(service=S, options=opt)
driver.get("http://fb.com")
driver.maximize_window()
actual_title = driver.title
print(actual_title)
actual_url = driver.current_url
print(actual_url)
time.sleep(5)
driver.close()