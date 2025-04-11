import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
time.sleep(2)

Returns=driver.find_element(By.XPATH,"//span[text()='Returns']")

act = ActionChains(driver)
#act.move_to_element(Returns).click().perform()
act.click(Returns).perform()
time.sleep(10)
