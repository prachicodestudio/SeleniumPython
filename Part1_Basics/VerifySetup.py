#import webdriver module from selenium package
from selenium import webdriver

#instantiate webdriver and launch Chrome browser
driver = webdriver.Chrome()

#open google.com web page
driver.get("https://www.google.com")

#close the browser window
driver.quit()
