#import webdriver module from selenium package
from selenium import webdriver # to interact with browser
#from selenium.webdriver.common.by import By  # To locate elements on the webpage
import time  # To add delays (for demonstration purposes)

#instantiate webdriver and launch Chrome browser
driver = webdriver.Chrome()

#maximise browser
driver.maximize_window()

#open url google.com
driver.get("https://www.google.com/")

#print title
print("First page:" + driver.title)

#swicth to new tab
#driver.switch_to.new_window("tab")

#switch to new window
driver.switch_to.new_window("window")

#open facebook.com url
driver.get("https://www.facebook.com/")

#print title
print("second tab:" + driver.title)

time.sleep(5)

#close face book tab
driver.close()

#get all open tabs and window handles
handles =driver.window_handles

#switch to google page
driver.switch_to.window(handles[0])
#print title
print("First page:" + driver.title)

#close browser
driver.quit()



