import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///D:/Other_Notes/Python%20Automation/Python%20Notes/Html%20Files/Linktext_PartialLinkText.html")
time.sleep(2)

#click on facebook link
#driver.find_element(By.LINK_TEXT,"facebook").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"book").click()

time.sleep(5)