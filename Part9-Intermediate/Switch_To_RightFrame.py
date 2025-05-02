from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch browser & maximise window
driver = webdriver.Chrome()
driver.maximize_window()

#open url
driver.get("C:/Users/ASUS/Downloads/iframe-practice-site/example/index.html")

#switch to right frame to fill form
driver.switch_to.frame(1) #use index to switch to right frame


# Click the button (this will trigger an alert)
button = driver.find_element(By.TAG_NAME, "button")
button.click()

# Handle the alert
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept() #to accept the alert

# Select from dropdown
dropdown = Select(driver.find_element(By.ID, "options"))
dropdown.select_by_visible_text("Option Two")


driver.switch_to.default_content() #switch back to main content

time.sleep(3)

#close browser
driver.quit()