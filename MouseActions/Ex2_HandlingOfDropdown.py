import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
time.sleep(2)

loginElement=driver.find_element(By.XPATH,"//span[text()='Login']");

act=ActionChains(driver)
act.move_to_element(loginElement).perform()
time.sleep(3)

#click on Gift cards from dropdown
driver.find_element(By.XPATH,"//li[text()='Gift Cards']").click();

time.sleep(10)

