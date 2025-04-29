import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(5)

#Enter UN
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
time.sleep(1)
#Enter PWD
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
time.sleep(1)
#click on login btn
driver.find_element(By.XPATH,"//input[@id='login-button']").click()

#title validation
actTilte=driver.title
expTitle="Swag Labs"

if actTilte==expTitle:
    print("TC Pass")
else:
    print("TC Fail")


time.sleep(10)