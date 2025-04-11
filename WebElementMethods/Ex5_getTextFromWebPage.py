import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

#get text from webpage
info=driver.find_element(By.XPATH,"//button[@type='submit']").text
print(info)

time.sleep(5)
