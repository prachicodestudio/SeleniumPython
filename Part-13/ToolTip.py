#import webdriver module from selenium package
from selenium import webdriver # to interact with browser
from selenium.webdriver.common.by import By  # To locate elements on the webpage
from selenium.webdriver import ActionChains # to perform mouse hover action on button to show tooltip
import time  # To add delays (for demonstration purposes)


#instantiate webdriver and launch Chrome browser
driver = webdriver.Chrome()

#maximise window
driver.maximize_window()

driver.implicitly_wait(10) #wait 10 seconds for web element to appear

#open  web page
driver.get("https://practice.expandtesting.com/tooltips")

#locate tool tip button
button1 = driver.find_element(By.ID,"btn1")
button2 = driver.find_element(By.ID,"btn2")
button3 = driver.find_element(By.ID,"btn3")
button4 = driver.find_element(By.ID,"btn4")
button5 = driver.find_element(By.ID,"btn5")

buttons = [button1,button2,button3,button4,button5]

for button in buttons:

    #create object of ActionsChains class
    actions = ActionChains(driver)

    # Move mouse pointer to the button
    actions.move_to_element(button).perform()
    # Small delay so tooltip becomes visible
    time.sleep(1)

    # Get tooltip text from the 'title' attribute of the button
    tooltip_text = button.get_attribute("title")

    print(tooltip_text)

#close
driver.close()