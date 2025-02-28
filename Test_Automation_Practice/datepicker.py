from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

# Switch to frame
driver.switch_to.frame(0)

# Insert date in input box - mm/dd/yyyy
driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("05/30/2022")