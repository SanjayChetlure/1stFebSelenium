import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

# result=driver.find_element(By.XPATH,"//a[text()='Create new account']").is_displayed()
# print(result)


try:
    result = driver.find_element(By.XPATH, "//a[text()='Create new account']").is_displayed()
    print("Element is present")
except NoSuchElementException:
    print("Element is not present")


time.sleep(10)