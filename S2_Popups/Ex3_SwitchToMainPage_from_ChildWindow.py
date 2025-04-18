import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://skpatro.github.io/demo/links/")
driver.implicitly_wait(10)
time.sleep(2)

#click on NewTab btn from main page
driver.find_element(By.XPATH,"//input[@name='NewTab']").click()

#get child Window ID
allIds=driver.window_handles        #[mainPageID[0], childWindowID[1]]

#switch to child window
driver.switch_to.window(allIds[1])

#click on Training link from child window
driver.find_element(By.XPATH,"(//span[text()='Training'])[1]").click()
time.sleep(3)

#switch to main page/window
driver.switch_to.window(allIds[0])
time.sleep(3)

#click on NewTWindow btn from main page
driver.find_element(By.XPATH,"//input[@name='NewWindow']").click()


time.sleep(10)