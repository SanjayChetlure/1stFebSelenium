import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(2)

driver.find_element(By.XPATH,"//button[starts-with(@id,'u_0_5')]").click()
#//tagname[starts-with(@attributeName,'partialAttributeValue')]

time.sleep(10)

