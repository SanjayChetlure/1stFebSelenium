import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver=webdriver.Chrome(chrome_options)
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

#Handle Alert Popup
#driver.switch_to.alert.accept()

time.sleep(10)