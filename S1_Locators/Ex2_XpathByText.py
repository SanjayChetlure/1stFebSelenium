import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(4)

# # click on forgotten pwd link
# driver.find_element(By.XPATH,"//a[text()='Forgotten password?']").click()

# click on Create New Acc link
driver.find_element(By.XPATH,"//a[text()='Create new account']").click()

time.sleep(4)

