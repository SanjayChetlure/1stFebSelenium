import time
from selenium import webdriver

#Open Browser
driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://www.google.com/")

#get Title
actTitle=driver.title
print(actTitle)
if actTitle=="Google":
    print("Pass")
else:
    print("Fail")

print(driver.title)


#get Current URL
actURL=driver.current_url
print(actURL)

print(driver.current_url)