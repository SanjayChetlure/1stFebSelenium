import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/r.php?entry_point=login")
time.sleep(2)

month=driver.find_element(By.XPATH,"//select[@id='month']")

#Open listbox option
month.click()
time.sleep(2)

#Navigate to last option using End key
month.send_keys(Keys.END)
time.sleep(2)

#Navigate to Nov Option using key -> ARROW_UP
month.send_keys(Keys.ARROW_UP)
time.sleep(2)

#Select option using Key -> Enter
month.send_keys(Keys.ENTER)

time.sleep(10)

