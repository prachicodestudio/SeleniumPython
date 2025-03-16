from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

#maximise browser window
driver.maximize_window()

# Open Google
driver.get("https://www.google.com")
print("Google opened.")

# Locate the search box and type 'Selenium'
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
print("Typed 'Selenium' in the search box.")

# Pause for suggestions to load (simple time.sleep for now)
time.sleep(2)

# Find all suggestions
suggestions = driver.find_elements(By.XPATH,"//ul[@role='listbox']//li")

# Print all suggestions
print("Search suggestions:")
for suggestion in suggestions:
    print(suggestion.text)


# Wait for result page to load
time.sleep(3)

# Close browser
driver.quit()
