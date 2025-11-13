#import webdriver module from selenium package
from selenium import webdriver # to interact with browser
from selenium.webdriver.common.by import By  # To locate elements on the webpage
import time  # To add delays (for demonstration purposes)

#instantiate webdriver and launch Chrome browser
driver = webdriver.Chrome()

#maximise window
driver.maximize_window()

driver.implicitly_wait(10) #wait for web element to appear

#open  web page
driver.get("https://practice.expandtesting.com/dynamic-table")

row_list = driver.find_elements(By.XPATH,"//table[@class='table table-striped']/tbody/tr")

rows = len(row_list)
print(rows)

for r in range(1, rows +1 ):  # Example: 1,2, 3,4
    cell = driver.find_element(By.XPATH,f"//table[@class='table table-striped']/tbody/tr[{r}]/td[1]")
    if cell.text == "Chrome":
        cpu = driver.find_element(By.XPATH,f"//table[@class='table table-striped']/tbody/tr[{r}]/td[contains(text(),'%')]")
        print(cpu.text)

        #compare chrome cup usage with chrome cpu in yellow label
        #find yellow label
        chrome_cpu = driver.find_element(By.ID, "chrome-cpu")
       # print("yellow lable chrome cpu:" + chrome_cpu.text)
        if cpu.text in chrome_cpu.text:
            print("chrome cpu usage matching")
        else:
            print("chrome cpu usage not matching")

        #stop for loop once chrome process is found
        break

#close browser
driver.quit()