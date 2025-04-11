import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

driver.save_screenshot("D:\\1st Feb Python Automation\\Screenshots\\img2.png")

time.sleep(5)
