import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
time.sleep(2)

mainPage=driver.current_window_handle

print(mainPage)

# driver.switch_to.window()

time.sleep(10)
