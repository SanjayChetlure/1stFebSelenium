import time
from selenium import webdriver

#Open Browser
driver=webdriver.Firefox()

#Open Application
driver.get("https://www.google.com/")

time.sleep(5)

#close Browser
driver.close()
# driver.quit()

