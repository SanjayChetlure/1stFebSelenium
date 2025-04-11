import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

# #click on forgotten pwd link
# driver.find_element(By.XPATH,"//a[contains(text(),'password')]").click()

#click on create new acc link
driver.find_element(By.XPATH,"//a[contains(text(),'new')]").click()

time.sleep(4)