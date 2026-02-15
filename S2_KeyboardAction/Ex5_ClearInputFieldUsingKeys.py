
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com")
time.sleep(2)

UN=driver.find_element(By.XPATH,"//input[@name='email']")
UN.send_keys("xyz")
time.sleep(2)

#Select All & Delete
UN.send_keys(Keys.CONTROL + "a")
UN.send_keys(Keys.DELETE)
time.sleep(2)

#Enter new value
UN.send_keys("abc")
time.sleep(10)