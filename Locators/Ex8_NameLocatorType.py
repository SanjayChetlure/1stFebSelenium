import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///D:/Other_Notes/Python%20Automation/Python%20Notes/Html%20Files/Name.html")
time.sleep(2)

#Enter FN
driver.find_element(By.NAME,"abc123").send_keys("abc")
#Enter LN
driver.find_element(By.NAME,"abc123").send_keys("xyz")
time.sleep(15)
