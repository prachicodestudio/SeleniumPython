# Import required libraries
from selenium import webdriver  # To interact with the browser
from selenium.webdriver.common.by import By  # To locate elements on the webpage
import time  # To add delays (for demonstration purposes)

# Initialize WebDriver and launch chrome browser
driver = webdriver.Chrome()
print("Browser opened")

#maximise browser window
driver.maximize_window()
print("Browser maximised")

#open url
# Open the Web Elements page
driver.get("http://uitestingplayground.com/alerts")
print("url opened")

############################Simple Alert#################################
# #find alert button
# alert_button = driver.find_element(By.ID, "alertButton")
#
# #click on alert button
# alert_button.click()
#
# #switch focus to alert pop-up
# alert = driver.switch_to.alert
#
# #print alert message
# print("Simple alert message:", alert.text)
#
# time.sleep(5)
# #click on alter ok button by accepting alert
# alert.accept()



############################Confirmation Alert#################################3

#find confirmation alert button
# confirm_alert_button = driver.find_element(By.ID, "confirmButton")
#
# #click on alert button
# confirm_alert_button.click()
#
# #switch focus to alert pop-up
# confirm_alert = driver.switch_to.alert
#
# #print alert message
# print("Confirm alert message:", confirm_alert.text)
#
# time.sleep(5)
# #click on alter ok button by accepting alert
# #confirm_alert.accept() #accept to click on ok
# confirm_alert.dismiss() #to cancel alert
# time.sleep(3)
#
# simple_alert = driver.switch_to.alert #switch focus to simple alert
# time.sleep(3)
# simple_alert.accept()


########################### Handling Prompt Alert ###########################

# Find and click the Prompt Alert button
prompt_alert_button = driver.find_element(By.ID, "promptButton")
prompt_alert_button.click()
print("Prompt alert opened!")

# Switch focus to the prompt alert
prompt_alert = driver.switch_to.alert

# Print alert message
print("Prompt alert message:", prompt_alert.text)

time.sleep(2)  # Wait for visibility

# Enter text in the prompt alert
prompt_alert.send_keys("Hello Selenium!")
print("Entered text in prompt alert.")

time.sleep(2)  # Wait to see input

# Accept the prompt alert
prompt_alert.accept()
print("Prompt alert accepted!")
time.sleep(3)

second_alert = driver.switch_to.alert
print("second alert message you entered:", second_alert.text)

time.sleep(3)
second_alert.accept()
# OR dismiss the alert instead of accepting
# prompt_alert.dismiss()
# print("Prompt alert dismissed!")


#close browser
driver.quit()
