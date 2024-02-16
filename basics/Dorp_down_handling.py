import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select

Ser = Service(executable_path='D:\\Selenium Drivers\\geckodriver-v0.33.0-win64\\geckodriver.exe')
driver = webdriver.Firefox(service = Ser)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0_0')]").click()
time.sleep(5)
dd_month = driver.find_element(By.NAME,"birthday_month")
sel = Select(dd_month)
first_option = sel.first_selected_option
print(first_option.text)
sel.select_by_visible_text("Aug")
time.sleep(5)
sel.select_by_value("1")
time.sleep(5)
sel.select_by_index(5)
