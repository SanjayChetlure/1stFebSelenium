import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")

allLinks=driver.find_elements(By.XPATH,"//a")
print(len(allLinks))

for i in allLinks:
    print(i.text)

time.sleep(10)

