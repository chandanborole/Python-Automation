from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

# Maximize window
driver.maximize_window()

# Open application
driver.get("https://testautomationpractice.blogspot.com/")

# Fill name
driver.find_element(By.ID, "name").send_keys("Test Automation")

# Fill email
driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("testautomation@gmail.com")

# Fill phone number
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Phone']").send_keys("0123456789")

# Fill address
driver.find_element(By.ID, "textarea").send_keys("Python Automation")

# Select gender
driver.find_element(By.CSS_SELECTOR, "input.form-check-input[value='female']").click()
