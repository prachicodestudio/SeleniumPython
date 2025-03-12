from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the Web Elements page
driver.get("https://dmytro-ch21.github.io/html/web-elements.html")

# Select radio buttons (BMW and Tesla)
bmw_radio = driver.find_element(By.ID, "radio2")
tesla_radio = driver.find_element(By.ID, "radio4")

# Click to select BMW and Tesla
bmw_radio.click()
print("BMW selected:", bmw_radio.is_selected())

tesla_radio.click()
print("Tesla selected:", tesla_radio.is_selected())

# Wait for 3 seconds
time.sleep(3)

# Close browser
driver.quit()
