import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element(By.XPATH,"//input[contains(@placeholder,'address or phone')]").send_keys("abc@gmail.com")
driver.find_element(By.XPATH,"//input[contains(@class,'_6luy _9npi')]").send_keys("nsdfhf9rr32r")
driver.find_element(By.XPATH,"//button[contains(@class,'4jy1 selected _51sy')]").click()

time.sleep(4)