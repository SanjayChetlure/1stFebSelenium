import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")
time.sleep(2)

#Switch to Frame
driver.switch_to.frame("iframeResult")

#click on Date & Time Btn from Iframe
driver.find_element(By.XPATH,"//button[contains(text(),'Click me')]").click()
time.sleep(3)

#Switch to Main Page
driver.switch_to.parent_frame()
# driver.switch_to.default_content()

#click on Open menu btn from Main Page
driver.find_element(By.XPATH,"//a[@id='menuButton']").click()


time.sleep(10)

