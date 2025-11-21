from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os #operating system module

# -----------------------------------------
# STEP 1: Create screenshot folder
# -----------------------------------------
#C:\Users\ASUS\PycharmProjects\WebAutomationProject\ScreenShots
folder_path = r"C:\Users\ASUS\PycharmProjects\WebAutomationProject\ScreenShots"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# -----------------------------------------
# STEP 2: Launch Chrome
# -----------------------------------------

driver = webdriver.Chrome() #create object of webdriver
driver.maximize_window() # maximise browser window

# -----------------------------------------
# STEP 3: Open webpage
# -----------------------------------------

driver.get("https://www.saucedemo.com/")
time.sleep(2) # to load page properly

# -----------------------------------------
# FULL PAGE SCREENSHOT
# -----------------------------------------

full_page_path = folder_path + "\\fullpage.png"
#driver.save_screenshot(full_page_path)
driver.get_screenshot_as_file(full_page_path)

print("Full page screenshot saved at:", full_page_path)

# -----------------------------------------
# ELEMENT SCREENSHOT (login button)
# -----------------------------------------

element = driver.find_element(By.ID, "login-button")

element_path = folder_path + "\\login_button.png"
element.screenshot(element_path)

print("Element screenshot saved at:", element_path)

# -----------------------------------------
# LOGIN CREDENTIAL SECTION SCREENSHOT
# -----------------------------------------

element = driver.find_element(By.ID, "login_credentials")

element_path = folder_path + "\\section-login_credentials.png"
element.screenshot(element_path)

print("Section screenshot saved at:", element_path)


#close browser
driver.quit()


