import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.mobikwik.com/")
time.sleep(2)

#click on login btn
driver.find_element(By.XPATH,"(//span[text()='Login'])[1]").click()
time.sleep(2)

#enter mobile number
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("9999999999")


time.sleep(10)