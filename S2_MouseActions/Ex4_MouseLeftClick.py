import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(2)

cartElement=driver.find_element(By.XPATH,"//a[text()='Cart']");

act=ActionChains(driver)
# act.move_to_element(cartElement).perform()
# act.click().perform()

#act.move_to_element(cartElement).click().perform()

act.click(cartElement).perform()

time.sleep(10)

