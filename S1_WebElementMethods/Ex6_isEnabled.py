import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

result=driver.find_element(By.XPATH,"//button[@type='submit']").is_enabled()
print(result)
print(type(result))

if result:
    print("Element is Enabled")
else:
    print("Element is disabled")