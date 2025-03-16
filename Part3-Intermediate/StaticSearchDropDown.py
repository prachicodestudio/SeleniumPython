# Import required libraries
from selenium import webdriver  # To interact with the browser
from selenium.webdriver.common.by import By  # To locate elements on the webpage
import time  # To add delays (for demonstration purposes)

# Initialize WebDriver and launch chrome browser
driver = webdriver.Chrome()
print("Browser opened")

#maximise browser window
driver.maximize_window()

print("Browser maximised")

#open url
# Open the Web Elements page
driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
print("url opened")

#find custom dropdown web element
dropdown = driver.find_element(By.CLASS_NAME, "search-box")

#use javascript to scroll the web page to make dropdown visible
driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
print("scroll to dropdown")
time.sleep(5)
dropdown.click() #perform click action to open the dropdown

#enter text 'S'
dropdown.send_keys("S")
time.sleep(5)

#find SUV option from dropdown
option = driver.find_element(By.XPATH,"//div[@class='searchable-option' and text()='SUV']")
option.click()


time.sleep(5)

#close browser
driver.quit()
