import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

driver.find_element(By.XPATH,"//img[@class='fb_logo _8ilh img']").screenshot("D:\\1st Feb Python Automation\\Screenshots\\logo.png")

time.sleep(5)
