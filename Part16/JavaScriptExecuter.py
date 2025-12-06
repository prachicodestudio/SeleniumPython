from selenium import webdriver # to interact with browser
from selenium.webdriver.common.by import By  # To locate elements on the webpage
import time  # To add delays (for demonstration purposes)

#instantiate webdriver and launch chrome browser
driver = webdriver.Chrome()

#maximise browser window
driver.maximize_window()

# #1. scroll down by 600px
# #open url
# driver.get("https://practice.expandtesting.com/infinite-scroll")
# driver.execute_script("window.scrollBy(0,600);")  # scroll 600px

# #2. scroll down / infinite scroll
# #open url
# driver.get("https://practice.expandtesting.com/infinite-scroll")
#
# for i in range(10):
#     driver.execute_script("window.scrollBy(0,600);")  # scroll 600px
#     time.sleep(1)

#  #3. scroll up by 600px
#  #open url
# driver.get("https://practice.expandtesting.com/infinite-scroll")
# driver.execute_script("window.scrollBy(0,1200);")  # scroll 600px
# time.sleep(1)
#
# #scroll up by 600 px
# driver.execute_script("window.scrollBy(0,-600);")  # scroll 600px

#4. scroll into view
#  #open url
# driver.get("https://practice.expandtesting.com/large")
# element = driver.find_element(By.ID, "sibling-50.3")
# driver.execute_script("arguments[0].scrollIntoView(true);",element)

#5. Click by JS
# #open url
# driver.get("https://practice.expandtesting.com/dynamic-loading/1")
# start_btn = driver.find_element(By.XPATH,"//button[@class='btn btn-primary']")
# driver.execute_script("arguments[0].click();",start_btn)
#
# time.sleep(8)

#6. Input value using JS
# driver.get("https://practice.expandtesting.com/inputs")
# textbox = driver.find_element(By.ID,"input-text")
#
# driver.execute_script("arguments[0].scrollIntoView(true);",textbox)
# time.sleep(2)
# driver.execute_script("arguments[0].value='Hello Python!';",textbox)

#7. Highlight Web Element
# driver.get("https://practice.expandtesting.com/challenging-dom")
# element = driver.find_element(By.XPATH,"(//a[text()='Edit'])[3]")
#
# #scroll till web element
# driver.execute_script("arguments[0].scrollIntoView(true);",element)
#
# #Highlight using border
# driver.execute_script("arguments[0].style.border='3px solid red';",element)

#8. Flash web element

# driver.get("https://practice.expandtesting.com/tables")
# cell = driver.find_element(By.XPATH,"//table[@id='table1']//tr[1]//td[2]")
#
# #scroll till web element cell
# driver.execute_script("arguments[0].scrollIntoView(true);",cell)
#
# for i in range(20):
#     driver.execute_script("arguments[0].style.backgroundColor='yellow';",cell)
#     time.sleep(0.1)
#
#     driver.execute_script("arguments[0].style.backgroundColor='white';", cell)
#     time.sleep(0.1)

#9. Javascript alerts (custom alerts)
# driver.get("https://practice.expandtesting.com/")
#
# #Generate alert u sing JS (custom alert)
# driver.execute_script("alert('This is custom alert from Python JS Executor!')")
# time.sleep(4)
#
# driver.switch_to.alert.accept()

# 10. Get Title / URL / Domain
driver.get("https://practice.expandtesting.com/")

#get title
# title = driver.execute_script("return document.title;")
# print("Title:",title)
#
# #get url
# url = driver.execute_script("return document.URL;")
# print("URL:",url)
#
# #get domain
# domain = driver.execute_script("return document.domain;")
# print("DOMAIN:",domain)

#11. Refresh Browser
# driver.get("https://practice.expandtesting.com/")
# driver.execute_script("history.go(0)")

#12.Get Page Inner Text (Full visible Text of Page)
text = driver.execute_script("return document.documentElement.innerText;")
print(text)
time.sleep(2)
#close browser
driver.quit()


