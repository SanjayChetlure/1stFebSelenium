import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/1st%20Feb%20Python%20Automation/Selenium/Html%20Files/WebTable.html")
time.sleep(2)

value=driver.find_element(By.XPATH,"//table[@id='abc123']//tr[3]/td[2]").text
print(value)

time.sleep(10)

