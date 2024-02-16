import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

#ser = Service(executable_path='D:\\Selenium Drivers\\chromedriver-win64\\chromedriver.exe')
#driver = webdriver.Chrome(service=ser)

s = Service(executable_path='D:\\Selenium Drivers\\geckodriver-v0.33.0-win64\\geckodriver.exe')
driver = webdriver.Firefox(service = s)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[@data-testid='open-registration-form-button']").click()
driver.find_element(By.ID,'cookie-use-link').click()
print(driver.title)
parent_window = driver.current_window_handle
child_window = driver.window_handles

for child in child_window:
    if child != parent_window:
        driver.switch_to.window(child)
        print(driver.title)
        time.sleep(5)
        child_win_text = driver.find_element(By.XPATH,"//span[contains(text(), 'what does this policy cover')]").text
        print(child_win_text)
        #driver.close()
time.sleep(5)
driver.switch_to.window(parent_window)
driver.find_element(By.NAME,"firstname").send_keys('ragul')
time.sleep(5)
#driver.close()
driver.quit()