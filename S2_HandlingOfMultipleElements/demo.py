import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///D:/6th%20July%202024/Selenium/html%20files/MultipleCheckboxes.html")
time.sleep(2)

allCheckBoxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for singleCheckbox in allCheckBoxes:
    singleCheckbox.click()
    time.sleep(1)

allCheckBoxes.reverse()

for singleCheckbox in allCheckBoxes:
    singleCheckbox.click()
    time.sleep(1)





time.sleep(10)