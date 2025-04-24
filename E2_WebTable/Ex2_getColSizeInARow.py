import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/1st%20Feb%20Python%20Automation/Selenium/Html%20Files/WebTable.html")
time.sleep(2)

allCols=driver.find_elements(By.XPATH,"//table[@id='abc123']//tr[3]/td")
print(len(allCols))

#for headers
allCols1=driver.find_elements(By.XPATH,"//table[@id='abc123']//tr[1]/th")
print(len(allCols1))


time.sleep(10)

