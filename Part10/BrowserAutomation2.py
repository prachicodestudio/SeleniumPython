from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser & maximize window
driver = webdriver.Chrome()
driver.maximize_window()

# Open the URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(2)
## Get the unique ID of the currently active browser window
parent_window_id = driver.current_window_handle
print("Parent window id:", parent_window_id)

#find link OrangeHRM, Inc webelement and click on it
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

# Get all window handles (IDs) after new window is opened
# List order :
# window_ids[0] → This is usually the parent window (the first window you opened).
# window_ids[1] → This is typically the child window (new window/tab that opened after clicking a link or button).
list_Window_ids= driver.window_handles
print("All windows ids:", list_Window_ids)

# Switch to the new (child) window
for window_id in list_Window_ids:
    if window_id != parent_window_id:
        driver.switch_to.window(window_id)
        print("Switched to child window with ID:", window_id)

#7.	Verify the window by checking title
expected_title = "Human Resources Management Software | OrangeHRM HR Software"
if driver.title == expected_title:
    print("Switched to the correct window.")
else:
    print("This is not the expected window.")

time.sleep(2)

#locate contact sale webelement and click on it
driver.find_element(By.XPATH,"(//button[@class='btn btn-ohrm btn-free-demo'])[2]").click()
driver.close() #closes only the currently active window that is child window

#switch back to original / parent window
driver.switch_to.window(parent_window_id)
#enter username
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")


time.sleep(5)
driver.quit() # quit() method closes all the browser window opened by the webdriver and
              # ends the webdriver session and clean up everything