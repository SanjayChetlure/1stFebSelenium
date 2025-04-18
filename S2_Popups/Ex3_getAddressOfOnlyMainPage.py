import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://skpatro.github.io/demo/links/")
driver.implicitly_wait(10)
time.sleep(2)

#click on NewTab btn from main page
driver.find_element(By.XPATH,"//input[@name='NewTab']").click()

#get main Window ID
mainPageId=driver.current_window_handle
print(mainPageId)

time.sleep(10)