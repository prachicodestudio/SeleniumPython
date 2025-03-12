from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the Web Elements page
driver.get("https://dmytro-ch21.github.io/html/web-elements.html")

# Locate multi-select dropdown
multi_select = Select(driver.find_element(By.ID, "multiSelect"))

#verify if dropdown is multi select
if multi_select.is_multiple:
    print("dropdown is multi select")
else:
    print("dropdown is not multi select")


# Select multiple options
multi_select.select_by_visible_text("Volvo")
multi_select.select_by_visible_text("Audi")
time.sleep(5)
# Deselect an option
multi_select.deselect_by_visible_text("Volvo")

# Get all selected options
selected_options = multi_select.all_selected_options
for option in selected_options:
    print("Selected:", option.text)


time.sleep(5)
#deselect all
multi_select.deselect_all()

#print all the option of the dropdown
allOptions = multi_select.options

print("-------------All options in multi select dropdown-------------------")
for option in allOptions:
    print(option.text)


# Wait for 3 seconds
time.sleep(3)

# Close browser
driver.quit()
