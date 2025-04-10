
# Import required libraries
from selenium import webdriver  # To interact with the browser
from selenium.webdriver.common.by import By  # To locate elements on the webpage
import time  # To add delays (for demonstration purposes)

#https://practice.expandtesting.com/

# Initialize WebDriver and launch chrome browser
driver = webdriver.Chrome()
print("Browser opened")

#maximise browser window
driver.maximize_window()
print("Browser maximised")

#open url
driver.get("https://practice.expandtesting.com/")

#delay of 3 sec to load page properly
time.sleep(3)

#find test login page link
#link = driver.find_element(By.LINK_TEXT,"Test Login Page")
link = driver.find_element(By.PARTIAL_LINK_TEXT,"Test Login")

# Scroll to the element using JavaScript
driver.execute_script("arguments[0].scrollIntoView(true);", link)

time.sleep(2)

link.click()

time.sleep(5)

#close browser
driver.quit()