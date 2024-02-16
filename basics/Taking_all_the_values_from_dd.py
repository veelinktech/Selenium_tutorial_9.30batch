import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0_0')]").click()
year_dd = driver.find_element(By.ID,"year")
sel = Select(year_dd)
year_li = sel.options
print(len(year_li))

#print(year_li[2].text)

for i in year_li:
    print(i.text)

time.sleep(5)