from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch browser & maximise window
driver = webdriver.Chrome()
driver.maximize_window()

#open url
driver.get("file:///C:/Users/ASUS/Downloads/iframe-practice-site/example/nested-frame.html")

time.sleep(1)

driver.switch_to.frame("parentFrame")

driver.switch_to.frame("childFrame")

#locate child frame text
childText = driver.find_element(By.ID,"childText")

print("child frame text:",childText.text)

driver.switch_to.default_content() #switch to main page
print(driver.find_element(By.TAG_NAME,"h1").text) #read heading of main page and print
time.sleep(3)

driver.quit()