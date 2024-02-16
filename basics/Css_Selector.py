from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

s = Service(executable_path='D:\\Selenium Drivers\\geckodriver-v0.33.0-win64\\geckodriver.exe')
driver = webdriver.Firefox(service = s)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.CSS_SELECTOR,'#email').send_keys("ragul")
driver.find_element(By.CSS_SELECTOR,"input[name='pass']").send_keys("ragul@123")
t1 = driver.find_element(By.CSS_SELECTOR,"h2._8eso").text
print(t1)