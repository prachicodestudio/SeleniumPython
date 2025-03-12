# Import required libraries
from selenium import webdriver  # To interact with the browser
from selenium.webdriver.common.by import By  # To locate elements on the webpage
from selenium.webdriver.support.ui import Select  # To handle drop-down menus
import time  # To add delays (for demonstration purposes)

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the Web Elements page
driver.get("https://dmytro-ch21.github.io/html/web-elements.html")

# Locate the single-select dropdown
#dropdown = Select(driver.find_element(By.ID, "carBrands"))
dropdown = Select(driver.find_element(By.ID,"carBrands"))

#check if dropdown is multiselect
if dropdown.is_multiple:
    print("this dropdown is multiselect")
else:
    print("This dropdown is not multiselect")

# Select options by visible text, value, and index
dropdown.select_by_visible_text("Mercedes")
print("Selected option:", dropdown.first_selected_option.text)


time.sleep(2)

dropdown.select_by_value("audi")
print("Selected option:", dropdown.first_selected_option.text)

time.sleep(2)

dropdown.select_by_index(1)  # Index starts from 0
print("Selected option:", dropdown.first_selected_option.text)

# Wait for 3 seconds
time.sleep(3)

# Close browser
driver.quit()
