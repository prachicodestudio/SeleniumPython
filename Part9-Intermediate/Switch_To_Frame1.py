from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

#open url
driver.get("C:/Users/ASUS/Downloads/iframe-practice-site/example/index.html")

#switch to left frame to fill form
driver.switch_to.frame("leftFrame")

#find name and fill name
driver.find_element(By.NAME,"name").send_keys("Prachi")

#find email and fill email
driver.find_element(By.NAME,"email").send_keys("prachi@exampple.com")

driver.switch_to.default_content() #switch back to main content

time.sleep(3)
#close browser
driver.quit()