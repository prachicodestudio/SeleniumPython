#import webdriver module
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#instantiate webdriver and launch chrome browser
driver = webdriver.Chrome()

#maximise browser
driver.maximize_window()


#open url
driver.get("https://dmytro-ch21.github.io/html/web-elements.html")

#fetch window title and print
print("window title:",driver.title)

#fetch url and print
print("url:",driver.current_url)

# #find check box
# ford_checkbox = driver.find_element(By.ID,"option1")
#
# if not ford_checkbox.is_selected():
#     ford_checkbox.click() #select ford checkbox
#
#
# bmw_checkbox = driver.find_element(By.ID,"option2")
# if not bmw_checkbox.is_selected():
#     bmw_checkbox.click() #select ford checkbox
#
#
# #verify selection
# print("Is ford selected:",ford_checkbox.is_selected())
# print("Is BMW selected:",bmw_checkbox.is_selected())

#select multiple checboxes using find_elements method
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()

time.sleep(5)
driver.quit()