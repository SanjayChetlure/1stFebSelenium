import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

driver.find_element(By.XPATH, "//a[text()='Create new account']").click()
time.sleep(2)

#Step1: identify listbox
month=driver.find_element(By.XPATH,"//select[@id='month']")   #WebElement Object
s=Select(month)

textValue=s.first_selected_option.text
print(textValue)


# selectedOption=s.first_selected_option
# textValue2=selectedOption.text
# print(textValue2)
#
# selectedOption=s.first_selected_option
# print(selectedOption.text)





time.sleep(10)
