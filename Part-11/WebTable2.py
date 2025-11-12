#import webdriver module from selenium package
from selenium import webdriver # to interact with browser
from selenium.webdriver.common.by import By  # To locate elements on the webpage
import time  # To add delays (for demonstration purposes)

#instantiate webdriver and launch Chrome browser
driver = webdriver.Chrome()

#maximise window
driver.maximize_window()

#open  web page
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3) #to load web page properly

#count total no. of rows
row_list = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
print("Rows:", len(row_list))

#count total no. of columns
column_list = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th")
print("Columns:", len(column_list))

#--------------------
# Step 3: Loop through rows and columns
# (Start from row 2 to skip header row)
# ---------------------------
for r in range(2, len(row_list) +1):  # Example: 2, 3,4,5,6,7
    for c in range(1, len(column_list) + 1):  # Example: 1, 2,3,4

        # Build dynamic XPath for each cell
        #// table / tbody / tr[{r}] / td[{c}]
        cell_xpath = f"//table[@name='BookTable']/tbody/tr[{r}]/td[{c}]"

        # Fetch cell element
        cell = driver.find_element(By.XPATH, cell_xpath)

        # Get text of each cell
        data = cell.text

        # Print the cell data
        print(data)  # print data

#close browser
driver.quit()