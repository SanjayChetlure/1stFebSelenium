import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

#click on create new acc link
driver.find_element(By.XPATH,"//a[text()='Create new account']").click()

time.sleep(3)
#Enter FN
driver.find_element(By.XPATH,"(//input[@type='text'])[1]").send_keys("abc")

#Enter LN
driver.find_element(By.XPATH,"(//input[@type='text'])[2]").send_keys("xyz")

#Enter mobile num
driver.find_element(By.XPATH,"(//input[@type='text'])[5]").send_keys("999999999")


time.sleep(10)