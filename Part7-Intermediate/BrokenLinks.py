
# Import required libraries
from selenium import webdriver  # To interact with the browser
from selenium.webdriver.common.by import By  # To locate elements on the webpage
import time  # To add delays (for demonstration purposes)
import requests


# Initialize WebDriver and launch chrome browser
driver = webdriver.Chrome()
print("Browser opened")

#maximise browser window
driver.maximize_window()
print("Browser maximised")

#open url
#driver.get("https://practice.expandtesting.com/")
driver.get("http://www.deadlinkcity.com/")

#delay of 3 sec to load page properly
time.sleep(3)

# Get all <a> tags
#links = driver.find_elements(By.TAG_NAME, "a")
links = driver.find_elements(By.XPATH,"//a")
print(f"Total links found: {len(links)}")
# Check if the link is broken


# Loop through all collected <a> link elements
for link in links:
    # Get the URL from the 'href' attribute of the <a> tag
    url = link.get_attribute("href")

    # Make an HTTP HEAD request to the given URL
    try:
        response = requests.head( url,timeout=5 ) #timeout = Maximum time (in seconds) to wait for a response. Prevents long hang time.
        if response.status_code >= 400:
            print("Broken Link")
        else:
            print("Valid Link")


    except Exception as e:
            print(f"Error happened: {e}")



time.sleep(3)
#close browser
driver.quit()


