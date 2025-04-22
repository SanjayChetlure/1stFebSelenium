import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(2)
driver.implicitly_wait(10)

#Enter Mobile Name
driver.find_element(By.XPATH,"//input[@class='Pke_EE']").send_keys("redmi 13 5g")

#click on search icon
driver.find_element(By.XPATH,"//button[@class='_2iLD__']").click()

#get Reviews
value=driver.find_element(By.XPATH,"((//div[@class='tUxRFH'])[1]//span)[8]").text
print(value)

time.sleep(10)

