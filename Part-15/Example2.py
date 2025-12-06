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

#switch to new tab
driver.switch_to.new_window("tab")

#open youtube.com
driver.get("https://www.youtube.com/")
print("New Tab page:" + driver.title)

#switch to new window
driver.switch_to.new_window("window")
driver.get("https://www.facebook.com/")
print("New Window:" + driver.title)

#get all open window/tab handles
handles = driver.window_handles
print("\n All windows/tab handles", handles)


#
# #Switching tab/window using handles
# #switch to google page
# driver.switch_to.window(handles[0])
# print("Web page at 0 index", driver.title)
#
# driver.switch_to.window(handles[1])
# print("Web page at 1 index", driver.title)
#
#
# driver.switch_to.window(handles[2])
# print("Web page at 3 index", driver.title)


#Switching by Title
target_title = "YouTube"

for h in handles:
    driver.switch_to.window(h)
    if driver.title==target_title:
        print("Switched to page title", driver.title)
        time.sleep(5)
        break

time.sleep(2)

# SWITCH TO FACEBOOK VIA URL

target_url = "https://www.facebook.com/"

for h in handles:
    driver.switch_to.window(h)
    if driver.current_url.startswith(target_url):
        print("\nSwitched to (by URL):", driver.title)
        break

time.sleep(2)

# CLOSE ONLY FACEBOOK WINDOW

if driver.title == "Facebook – log in or sign up":  # title may change
    driver.close()
    print("\nFacebook window closed.")

time.sleep(2)


#close browser
driver.quit()

