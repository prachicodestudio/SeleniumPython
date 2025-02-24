#import webdriver module from selenium package
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

#instantiate webdriver and launch Chrome browser
driver = webdriver.Chrome()

#maximise browser window
driver.maximize_window()

# Navigate to saucedemo website - open url
driver.get("https://www.saucedemo.com")
time.sleep(2) #wait for 2 seconds to let the page load

#Find all input fields (Username & Password) using find_elements()
#input_fields = driver.find_elements(By.TAG_NAME,"input")
input_fields = driver.find_elements(By.XPATH,"//input")

#find index of username and password
# print(input_fields[0].get_attribute('id'))
# print(input_fields[1].get_attribute('id'))
# print(input_fields[2].get_attribute('id'))
#
# index = 0
# for field in input_fields:
#     print(f"Index:{index}: {field.get_attribute('id')}")
#     index=index+1
#print(len(input_fields))

#enter username
input_fields[0].send_keys("standard_user")

#enter password
input_fields[1].send_keys("secret_sauce")

#click on login button
input_fields[2].click()

#list all the products
products = driver.find_elements(By.XPATH,"//div[@class='inventory_item_name ']")

print("Product list")

for product in products:
    print(product.text)  #text method to extract visible text

# #locate user name web element
# username = driver.find_element(By.NAME,"user-name")
#
# #enter username
# username.send_keys("standard_user")
time.sleep(3) #wait for 3 seconds

#close browser
driver.quit()