# Datepicker from dropdown

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.maximize_window()

# Open date picker
driver.find_element(By.XPATH,"//input[@id='dob']").click()

# Select month - used select class
datepicker_month=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
datepicker_month.select_by_visible_text("Dec")  # month

# Select year - used select class
datepicker_year=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
datepicker_year.select_by_visible_text("1990")

alldates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for date in alldates:
    if date.text=="25":
        date.click()
        break