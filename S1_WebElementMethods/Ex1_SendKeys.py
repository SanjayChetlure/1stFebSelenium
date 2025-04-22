import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

#apr1
#driver.find_element(By.XPATH,"//input[@id='email']").send_keys("abc")

#apr2
un=driver.find_element(By.XPATH,"//input[@id='email']")
un.send_keys("abc")


time.sleep(5)
