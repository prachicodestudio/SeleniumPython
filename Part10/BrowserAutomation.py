from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser & maximize window
driver = webdriver.Chrome()
driver.maximize_window()

# Open the URL
driver.get("https://the-internet.herokuapp.com/windows")

## Get the unique ID of the currently active browser window
parent_window_id = driver.current_window_handle
print("Parent window id:", parent_window_id)

#locate click here link web element and then perform click action
driver.find_element(By.LINK_TEXT,"Click Here").click()

# Get all window handles (IDs) after new window is opened
list_Window_ids= driver.window_handles
print("All windows ids:", list_Window_ids)

# Switch to the new (child) window
for window_id in list_Window_ids:
    if window_id != parent_window_id:
        driver.switch_to.window(window_id)
        print("Switched to child window with ID:", window_id)

#7.	Verify the window by checking title
expected_title = "New Window"
if driver.title == expected_title:
    print("Switched to the correct window.")
else:
    print("This is not the expected window.")


#7.	Verify the window by checking the URL
expected_url = "https://the-internet.herokuapp.com/windows/new"
if driver.current_url == expected_url:
    print("Switched to the correct window.")
else:
    print("This is not the expected window.")

time.sleep(5)

#close browser window
driver.quit()

