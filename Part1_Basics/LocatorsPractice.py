#import webdriver module
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#instantiate webdriver and launch chrome browser
driver = webdriver.Chrome()

#maximise browser window
driver.maximize_window()

def successful_login():
    # open url
    driver.get("https://practice.expandtesting.com/login")

    # locate user name
    # find_element method is use to loacte first matching webelement
    # username = driver.find_element(By.ID,"username")
    # username = driver.find_element(By.TAG_NAME,"input")
    username = driver.find_element(By.CLASS_NAME, "form-control")
    # enter username
    username.send_keys("practice")

    # locate password
    password = driver.find_element(By.NAME, "password")

    # enter password
    password.send_keys("SuperSecretPassword!")

    time.sleep(3)  # wait for 3 sec

    # locate login button
    # login = driver.find_element(By.XPATH, "//button[@type='submit']")
    # login = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
    # login = driver.find_element(By.XPATH, "//button[@class='btn btn-bg btn-primary d-block w-100']")
    # login = driver.find_element(By.XPATH, "//button[text()='Login']")
    login = driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]")
    # click on login button
    login.click()

    time.sleep(10)
    link = driver.find_element(By.LINK_TEXT, "Expand Testing")
    link.click()

    time.sleep(3)  # wait for 3 sec


def forgotten_password():
    #open url
    driver.get("https://www.facebook.com/")
    time.sleep(5) #wait for 5 sec
    #locate forgotton password link
    # forgottonPwdLink = driver.find_element(By.LINK_TEXT,"Forgotten password?")
    # forgottonPwdLink.click()
   # driver.find_element(By.LINK_TEXT,"Forgotten password?").click()
    driver.find_element(By.PARTIAL_LINK_TEXT,"Forgotten").click()

    time.sleep(5)  #wait for 5 sec

    expected_title = "Forgotten Password | Can't Log In | google"

    #capture actual title of the web page
    actual_title = driver.title

    #verify actual and expected title
    if actual_title==expected_title:
        print("Test passed")
    else:
       # print("Test failed")
        print(f"Test failed. expected '{expected_title}' but got '{actual_title}'")
    #
    # #locate email and enter email
    # driver.find_element(By.XPATH,"(//input)[1]").send_keys("example@gmail.com")
    #
    # #locate password and enter password
    # driver.find_element(By.XPATH,"(//input)[2]").send_keys("password")

    #locat email input box
    driver.find_element(By.XPATH,"//input[@id='identify_email' and @name='email']").send_keys("example@gmail.com")
    time.sleep(5)

#forgotten_password()

def css_selector():
    # open url
    driver.get("https://practice.expandtesting.com/login")

    #find username
   # driver.find_element(By.CSS_SELECTOR,"input").send_keys("practice")
    #driver.find_element(By.CSS_SELECTOR,"[name='username']").send_keys("practice")
    driver.find_element(By.CSS_SELECTOR,"input.form-control").send_keys("practice")

    driver.find_element(By.CSS_SELECTOR,"#password").send_keys("SuperSecretPassword!")

    button = driver.find_element(By.CSS_SELECTOR,".btn.btn-bg.btn-primary.d-block.w-100")

    # Scroll into view using JavaScript
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    time.sleep(3)

    button.click()

def css_selector2():
    #open facebook url
    driver.get("https://www.facebook.com/")

    #find email inputbox
    #driver.find_element(By.CSS_SELECTOR,"div>input#email").send_keys("example@gmail.com")
    driver.find_element(By.CSS_SELECTOR,"div input#email").send_keys("example@gmail.com")

    time.sleep(5)

#css_selector()
css_selector2()
time.sleep(5)
#close browser
driver.quit()


