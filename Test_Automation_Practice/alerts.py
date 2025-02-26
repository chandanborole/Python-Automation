from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

# Click on alert with textbox
driver.find_element(By.XPATH, "//a[normalize-space()='Alert with Textbox']").click()

# Click on promptbox
driver.find_element(By.XPATH, "//button[normalize-space()='click the button to demonstrate the prompt box']").click()

# To switch to alert - First capture alert window in variable
alertwindow=driver.switch_to.alert

# To print text
print(alertwindow.text)

# To insert text in alert input box
alertwindow.send_keys("this is testalert")

# To click OK button
alertwindow.accept()

# To click cancel button
alertwindow.dismiss()

time.sleep(5)