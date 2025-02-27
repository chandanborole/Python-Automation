from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Create ChromeOptions - use for browser level setting (disable popup, headless mode)
ops=webdriver.ChromeOptions()

# Add parameter to disable notification at browser level
ops.add_argument("--disable-notifications")

# Pass ops variable
driver=webdriver.Chrome(options=ops)

driver.get("https://whatmylocation.com/")
driver.maximize_window()
