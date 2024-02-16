from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from DDF import XLReader

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
driver.implicitly_wait(30)
path = "C:\\Users\\pc\\Desktop\\DDF.xlsx"
rows = XLReader.total_rows(path,"Sheet3")
for r in range(2,rows+1):
    user_name = XLReader.read_Data(path,"Sheet3", r , 1)
    pass_word = XLReader.read_Data(path,"Sheet3", r, 2)

    driver.find_element(By.NAME,"username").send_keys(user_name)
    driver.find_element(By.NAME,"password").send_keys(pass_word)
    driver.find_element(By.XPATH,"//button[normalize-space(text()='Login')]").click()
    profile_name = driver.find_element(By.XPATH,"//p[text()='John William']").text
    if profile_name == "John William":
        XLReader.write_Data(path,"Sheet3", r,3,"Pass")
        driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
        driver.find_element(By.LINK_TEXT,"Logout").click()

    else:
        XLReader.write_Data(path, "Sheet3", r, 3, "Fail")
        driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()

driver.close()