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

#switch to alert
alt=driver.switch_to.alert

#getText from alert popup
value=alt.text
print(value)

#click on Cancel btn
#alt.dismiss()

#click on Ok btn from 1st alert
alt.accept()

#click on Ok btn from 2nd alert
alt.accept()

#Enter value in alert popup
#alt.send_keys("input")





time.sleep(10)