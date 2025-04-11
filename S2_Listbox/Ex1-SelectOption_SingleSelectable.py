import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

driver.find_element(By.XPATH, "//a[text()='Create new account']").click()
time.sleep(2)

#Step1: identify listbox
month=driver.find_element(By.XPATH,"//select[@id='month']")   #WebElement Object

#Step2: Create Object Select class
s=Select(month)

#3: call select class method
#s.select_by_visible_text("Jun")       #String Text
#s.select_by_value("8")                #String value
s.select_by_index(11)

time.sleep(5)