import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser=Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(service=ser)
driver.get('http://fb.com')
driver.maximize_window()
driver.implicitly_wait(30)
# Single attribute
driver.find_element(By.XPATH," //input[@aria-label='Email address or phone number']").send_keys('Raj@gmail.com')
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='pass']").send_keys('Raj@123')
time.sleep(5)

#text() function
actual_link=driver.find_element(By.XPATH,"//*[text()=' for a celebrity, brand or business.']").text
print(actual_link)
time.sleep(5)

actual_fp=driver.find_element(By.XPATH,"//a[text()='Forgotten password?']").text
print(actual_fp)
time.sleep(5)

# contains() text()
actual_fp1=driver.find_element(By.XPATH,"//a[contains(text(),'got')]").text
print(actual_fp1)
time.sleep(5)

# starts-with()  text()

actual_fp2=driver.find_element(By.XPATH,"//a[starts-with(text(),'Fo')]").text
print(actual_fp2)
time.sleep(5)

driver.find_element(By.XPATH,"//a[@data-testid='open-registration-form-button']").click()
time.sleep(5)


# Multiple attribute
driver.find_element(By.XPATH,"//input[@class='_8esa'][@value='2']").click()
time.sleep(10)