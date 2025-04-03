# Import required libraries
from selenium import webdriver  # To interact with the browser
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By  # To locate elements on the webpage
import time  # To add delays (for demonstration purposes)

# Initialize WebDriver and launch chrome browser
driver = webdriver.Chrome()
print("Browser opened")

#maximise browser window
driver.maximize_window()
print("Browser maximised")


#add wait for 10 sec
driver.implicitly_wait(10)

#open url
# Open the Web Elements page
driver.get("https://duckduckgo.com/")
print("url opened")

#time.sleep(5) #wait for 5 sec. for page load

#find search box web element
search_box = driver.find_element(By.NAME,"q")

#enter search string "selenium"
search_box.send_keys("selenium")

#press enter key to submit the search string
search_box.send_keys(Keys.RETURN)

time.sleep(5)
#Close browser
driver.quit()
