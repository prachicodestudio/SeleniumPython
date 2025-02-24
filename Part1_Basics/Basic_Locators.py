#import webdriver module from selenium package
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

#instantiate webdriver and launch Chrome browser
driver = webdriver.Chrome()

#maximise browser window
driver.maximize_window()

# Navigate to saucedemo website - open url
driver.get("https://www.saucedemo.com")
time.sleep(2) #wait for 2 seconds to let the page load

#locate user name web element
#username = driver.find_element(By.NAME,"user-name")

#relative xpath to locate username
#username = driver.find_element(By.XPATH,"//input[@id='user-name']")
#username = driver.find_element(By.XPATH,"//input[@type='text' and @id='user-name']")
#username = driver.find_element(By.XPATH,"(//input)[1]")


#locate user name by tag name
#username = driver.find_element(By.TAG_NAME,"input")
#username = driver.find_element(By.CSS_SELECTOR,"input")
#username = driver.find_element(By.CSS_SELECTOR,"#user-name")
# username = driver.find_element(By.CSS_SELECTOR,"div > input[id='user-name']")
username = driver.find_element(By.CSS_SELECTOR,"form input[id='user-name']")


#enter username
username.send_keys("standard_user")

#locate password web element
#password = driver.find_element(By.ID,"password")
password = driver.find_element(By.XPATH,"//input[@name='password']")

#enter password
password.send_keys("secret_sauce")

time.sleep(5) #wait for 5 seconds

#locate login button
#loginBtn = driver.find_element(By.XPATH,"//input[@id='login-button']")
#loginBtn = driver.find_element(By.XPATH,"//input[@id='login-button' or id='wrong id']")

#locate login button using class name
#loginBtn = driver.find_element(By.CLASS_NAME,"btn_action")
#loginBtn = driver.find_element(By.CSS_SELECTOR,".btn_action")
#loginBtn = driver.find_element(By.CSS_SELECTOR,'[id="login-button"]')
#loginBtn = driver.find_element(By.CSS_SELECTOR,"input.btn_action")
loginBtn = driver.find_element(By.CSS_SELECTOR,"form > input[type='submit']")


#click on login buttton
loginBtn.click()

time.sleep(2) #wait for 2 seconds

#contains() - locate add to cart button
#addToCart = driver.find_element(By.XPATH,"//button[contains(@id,'sauce-labs-bolt-t-shirt')]")
#addToCart.click()

#text() - locate web element sauce lab fleece jacket and perform click action
# product= driver.find_element(By.XPATH,"//div[text()='Sauce Labs Fleece Jacket']")
# product.click()

# find product link for Sauce Labs Backpack using By.LINK_TEXT
#productLink = driver.find_element(By.LINK_TEXT,"Sauce Labs Backpack")

# find product link for Sauce Labs Backpack using By.PARTIAL_LINK_TEXT
productLink = driver.find_element(By.PARTIAL_LINK_TEXT,"Backpack")

#perform click action on product link
productLink.click()

time.sleep(2) #wait for 5 seconds

#close browser
driver.quit()


