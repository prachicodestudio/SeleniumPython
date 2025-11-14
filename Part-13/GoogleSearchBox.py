#import webdriver module from selenium package
from selenium import webdriver # to interact with browser
from selenium.webdriver.common.by import By  # To locate elements on the webpage
from selenium.webdriver import ActionChains # to perform mouse hover action on button to show tooltip
import time  # To add delays (for demonstration purposes)

#instantiate webdriver and launch Chrome browser
driver = webdriver.Chrome()

#maximise window
driver.maximize_window()

#driver.implicitly_wait(10) #wait 10 seconds for web element to appear

#open  web page
driver.get("https://google.com")

#locate tool tip button
SearchBox = driver.find_element(By.NAME,"q")

actions = ActionChains(driver)

actions.move_to_element(SearchBox).perform()

tooltip_text = SearchBox.get_attribute("title")

if tooltip_text=="Search":
    print("Pass")
else:
    print("Fail")

#close browser
driver.quit()