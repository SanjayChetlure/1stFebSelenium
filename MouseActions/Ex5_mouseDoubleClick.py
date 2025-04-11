import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
time.sleep(2)

Element=driver.find_element(By.XPATH,"//button[text()='Double-Click Me To See Alert']");

act=ActionChains(driver)
#act.move_to_element(Element).perform()
# act.double_click().perform()

#act.move_to_element(Element).double_click().perform()

act.double_click(Element).perform()

time.sleep(10)

