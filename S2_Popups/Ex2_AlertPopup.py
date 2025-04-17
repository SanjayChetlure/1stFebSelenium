import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.guru99.com/test/delete_customer.php")
time.sleep(2)

#Enter customer ID
driver.find_element(By.XPATH,"//input[@name='cusid']").send_keys("123")
time.sleep(2)

#click on submit btn
driver.find_element(By.XPATH,"//input[@name='submit']").click()

#getText from alert popup
value=driver.switch_to.alert.text
print(value)

#click on Ok btn
#driver.switch_to.alert.accept()

#click on Cancel btn
driver.switch_to.alert.dismiss()



time.sleep(10)