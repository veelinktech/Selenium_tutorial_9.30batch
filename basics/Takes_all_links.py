import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Ser = Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service = Ser)
driver.get("http://www.rediff.com")
driver.maximize_window()
driver.implicitly_wait(30)
link_list = driver.find_elements(By.TAG_NAME,"a")
print(len(link_list))

'''for i in link_list:
    print(i.text)'''

'''for i in link_list:
    print(i.get_attribute('href'))'''

for i in link_list:
    print(i.text,"---->",i.get_attribute('href'))

time.sleep(5)