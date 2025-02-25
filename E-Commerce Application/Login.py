from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

# Open application
driver.get("https://naveenautomationlabs.com/opencart/")

# Maximize window
driver.maximize_window()

# Click my account
driver.find_element(By.XPATH, "//span[@class='hidden-xs hidden-sm hidden-md'] [contains(text(), 'My Account')]").click()

# Click login
driver.find_element(By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right'] //a[contains(text(), 'Login')]").click()

# Provide email address
driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("testautomation@gmail.com")

# Provide password
driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("Automation@123")
#driver.find_element(By.CSS_SELECTOR, "input#input-password").send_keys("Automation@123")

# Click login
driver.find_element(By.XPATH, "//input[@type='submit']").click()

time.sleep(3)

