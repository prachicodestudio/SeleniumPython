from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch browser & maximise window
driver = webdriver.Chrome()
driver.maximize_window()

#open url
driver.get("file:///C:/Users/ASUS/Downloads/iframe-practice-site/example/nested-frame.html")

time.sleep(1)

# Find all iframe elements with the name attribute 'parentFrame'
# This returns a list of matching elements (could be empty if none found)
iframes = driver.find_elements(By.NAME, "parentFrame")

# Check if the list 'iframes' is not empty
# In Python, a non-empty list is considered True (truthy), and an empty list is False (falsy)
if iframes:
    # If at least one iframe is found, switch to the iframe named 'parentFrame'
    # We can pass the name directly to switch_to.frame() as a shortcut
    driver.switch_to.frame("parentFrame")
else:
    # If no iframe with the name 'parentFrame' is found, print a message
    print("parentFrame not found")

#driver.switch_to.frame("parentFrame")

driver.switch_to.frame("childFrame")

#locate child frame text
childText = driver.find_element(By.ID,"childText")

print("child frame text:",childText.text)

#driver.switch_to.default_content() #switch to main page
#print(driver.find_element(By.TAG_NAME,"h1").text) #read heading of main page and print
driver.switch_to.parent_frame() #For moving one level up from a nested iframe.

iframes_parentFrame = driver.find_elements(By.TAG_NAME, "iframe")
print("Total iFrames in parent frame:", len(iframes_parentFrame))


#locate parent frame text
parentText = driver.find_element(By.TAG_NAME,"p")
print("parent frame text:", parentText.text)

driver.switch_to.default_content() #switch to main page

iframes = driver.find_elements(By.TAG_NAME, "iframe")
print("Total iFrames in main page:", len(iframes))

time.sleep(3)
driver.quit() #close browser