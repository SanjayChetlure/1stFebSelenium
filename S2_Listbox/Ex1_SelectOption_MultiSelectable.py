import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("file:///D:/6th%20July%202024/Selenium/html%20files/Sample4_Listbox.html")
time.sleep(2)

#Step1: identify listbox
selectCountry=driver.find_element(By.XPATH,"//select[@id='abc123']")   #WebElement Object

#Step2: Create Object Select class
s=Select(selectCountry)

#3: call select class method
s.select_by_visible_text("Ind")
s.select_by_visible_text("Aus")
#s.select_by_value()
s.select_by_index(2)


time.sleep(5)