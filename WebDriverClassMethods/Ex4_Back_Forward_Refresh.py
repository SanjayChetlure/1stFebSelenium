import time
from selenium import webdriver

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://www.google.com/")
time.sleep(3)
driver.get("https://www.facebook.com/")

time.sleep(4)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(4)
driver.refresh()


time.sleep(5)
