import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(2)

act=ActionChains(driver)

#Scroll down (1st para - 0 & 2nd para -> +ve pixel value)
act.scroll_by_amount(0,200).perform()

time.sleep(3)

#Scroll up (1st para - 0 & 2nd para -> -ve pixel value)
act.scroll_by_amount(0,-100).perform()


#Scroll right (1st para - +ve & 2nd para -> 0 pixel value)
#act.scroll_by_amount(100,0).perform()

#Scroll left (1st para - -ve & 2nd para -> 0 pixel value)
#act.scroll_by_amount(-100,0).perform()


time.sleep(10)

