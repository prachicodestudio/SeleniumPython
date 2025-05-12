from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

# Launch browser & maximize window
driver = webdriver.Chrome()
driver.maximize_window()

# Open the URL
driver.get("file:///C:/Users/ASUS/Downloads/iframe-practice-site/example/nested-frame.html")

time.sleep(1)

# Find all iframe elements with the name attribute 'parentFrame'
iframes = driver.find_elements(By.NAME, "parentFrame")

if iframes:
    # Switch to parent frame
    try:
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.NAME, "parentFrame"))
    )
    except:
        print("parent frame not found")


    # Now switch to child frame
    try:

        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.NAME, "childFrame"))
    )
    except:
        print("child frame not found")

    # Locate and print child frame text
    childText = driver.find_element(By.ID, "childText")
    print("child frame text:", childText.text)

    # Go back to parent frame
    driver.switch_to.parent_frame()

    # Count and print iFrames in parent frame
    iframes_parentFrame = driver.find_elements(By.TAG_NAME, "iframe")
    print("Total iFrames in parent frame:", len(iframes_parentFrame))

    # Locate and print parent frame text
    parentText = driver.find_element(By.TAG_NAME, "p")
    print("parent frame text:", parentText.text)

    # Switch to main content
    driver.switch_to.default_content()

    # Count and print iFrames in main page
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print("Total iFrames in main page:", len(iframes))

else:
    print("parentFrame not found")

time.sleep(3)
driver.quit()
