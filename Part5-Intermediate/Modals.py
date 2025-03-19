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
driver.get("https://practice-automation.com/modals/")
print("url opened")

#find simple modal button and perform click action
driver.find_element(By.ID, "simpleModal").click()

time.sleep(2) #wait to make modal visible

#find modal title
modal_title = driver.find_element(By.ID,"pum_popup_title_1318").text
print(f"Modal Title:{modal_title}")

#find modal content

modal_content= driver.find_element(By.XPATH, "(//div[@class='pum-content popmake-content'])[2]").text
print(f"Modal Content:{modal_content}")

time.sleep(3)
#close simple moddal
driver.find_element(By.XPATH,"(//button[@class='pum-close popmake-close'])[2]").click()

############################Form modal#######################################3

#find form modal button
form_modal_button = driver.find_element(By.ID, "formModal")
print("Form modal is opened")

#scroll to form modal button
driver.execute_script("arguments[0].scrollIntoView();", form_modal_button)

time.sleep(2)
form_modal_button.click() #click on form modal button

#enter name
driver.find_element(By.NAME,"g1051-name").send_keys("Prachi")

#enter email
driver.find_element(By.NAME,"g1051-email").send_keys("example@gmail.com")

#enter message
driver.find_element(By.XPATH,"//textarea[@name='g1051-message']").send_keys("This is sammple message!")
print("Browser closed.")

time.sleep(3)

driver.find_element(By.XPATH,"(//button[@class='pum-close popmake-close'])[1]").click()

#close browser
driver.quit()



