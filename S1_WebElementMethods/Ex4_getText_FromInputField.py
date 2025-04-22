import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

#get text from input field
un=driver.find_element(By.XPATH,"//input[@id='email']")

un.send_keys("abc")
time.sleep(2)

text=un.get_attribute("value")
print(text)

time.sleep(5)
