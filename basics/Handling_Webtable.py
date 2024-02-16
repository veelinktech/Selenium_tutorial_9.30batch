from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service(executable_path="D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa?src=gain_lose")
driver.maximize_window()
driver.implicitly_wait(30)

# Single column
f1 = driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[3]/td[1]").text
print(f1)
f2 = driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[3]/td[3]").text
print(f2)
print('======Entire row=====')
f3 = driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[3]").text
print(f3)
print('======Entire table======')
et = driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr")
print(len(et))

for i in et:
    print(i.text)