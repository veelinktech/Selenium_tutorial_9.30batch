import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("http://www.google.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.ID,"APjFqb").send_keys('selenium')
time.sleep(5)
opt_list = driver.find_elements(By.XPATH,"//div[@class='erkvQe']/div/ul/li")
print(len(opt_list))

#for i in opt_list:
#    print(i.text)

for i in opt_list:
    if i.text == "selenium maven dependency":
        i.click()
        break

time.sleep(5)