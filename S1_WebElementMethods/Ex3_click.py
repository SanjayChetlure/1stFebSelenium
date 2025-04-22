import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

#click on create new acc link
driver.find_element(By.XPATH,"//a[text()='Create new account']").click()
time.sleep(2)
#click on female radio button
driver.find_element(By.XPATH,"(//input[@class='_8esa'])[1]").click()

time.sleep(5)
