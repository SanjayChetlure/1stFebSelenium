import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/Other_Notes/Python%20Automation/Python%20Notes/Html%20Files/MultipleCheckboxes.html")
time.sleep(2)

allCheckboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(allCheckboxes))

for i in allCheckboxes:
    i.click()
    time.sleep(1)

time.sleep(10)

