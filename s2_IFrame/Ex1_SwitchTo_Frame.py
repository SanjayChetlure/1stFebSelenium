import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")
time.sleep(2)

#Switch to Frame
# element=driver.find_element(By.XPATH,"//iframe[@id='iframeResult']")
# driver.switch_to.frame(element)            #using WebElement

#driver.switch_to.frame(0)           #using int FrameIndex

driver.switch_to.frame("iframeResult")         #using String FrameId/FrameName


#click on Date & Time Btn
driver.find_element(By.XPATH,"//button[contains(text(),'Click me')]").click()


time.sleep(10)

