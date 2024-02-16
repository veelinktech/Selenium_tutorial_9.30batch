from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.rediff.com/')
driver.maximize_window()
driver.implicitly_wait(30)
actual_text1 = driver.find_element(By.XPATH,"//a[@title='Lightning fast free email']").text
print(actual_text1)
#driver.switch_to.frame('moneyiframe') # id or name
#driver.switch_to.frame(0) #index
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Rediff Money Widget']")) # webelement
actual_text2 = driver.find_element(By.XPATH,"//span[text()='BSE']").text
print(actual_text2)
driver.switch_to.default_content()
actual_text3 = driver.find_element(By.XPATH,"//a[text()='Money']").text
print(actual_text3)