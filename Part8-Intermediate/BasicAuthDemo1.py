import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#instantiate webdriver and launch chrome browser
driver = webdriver.Chrome()

#maximise browser window
driver.maximize_window()

#open url
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

#capture response of basic authentication

message = driver.find_element(By.TAG_NAME,"p").text

print("Response:", message)

#wait for 5 sec
time.sleep(5)

#close broswer
driver.quit()