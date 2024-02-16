from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

opt = Options()
opt.add_argument("--headless")
s = Service(executable_path='D:\\Selenium Drivers\\geckodriver-v0.33.0-win64\\geckodriver.exe')
driver = webdriver.Firefox(service = s,options = opt)
driver.get('http://www.google.com')
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.close()