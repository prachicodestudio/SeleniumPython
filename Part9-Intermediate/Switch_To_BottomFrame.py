from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch browser & maximise window
driver = webdriver.Chrome()
driver.maximize_window()

#open url
driver.get("C:/Users/ASUS/Downloads/iframe-practice-site/example/index.html")

time.sleep(1)

# Locate the bottom frame WebElement
bottom_frame = driver.find_element(By.XPATH, "//iframe[@name='bottomFrame']")
driver.switch_to.frame(bottom_frame)

# Read and print text inside the bottom frame
text_element = driver.find_element(By.TAG_NAME, "p")
print("Text from Bottom Frame:", text_element.text)

# Switch back to main content
driver.switch_to.default_content()

# Pause to observe
time.sleep(2)
driver.quit()