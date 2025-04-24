import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/1st%20Feb%20Python%20Automation/Selenium/Html%20Files/WebTable.html")
time.sleep(2)

allRows=driver.find_elements(By.XPATH,"//table[@id='abc123']//tr")
print(len(allRows))

time.sleep(10)

