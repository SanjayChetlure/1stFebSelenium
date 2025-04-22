import time
from selenium import webdriver

#Open Browser
driver=webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.minimize_window()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.fullscreen_window()
time.sleep(5)