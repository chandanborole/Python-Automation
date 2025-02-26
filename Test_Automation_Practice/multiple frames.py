from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

# switch to 1st frame
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
driver.switch_to.default_content()  # go back to main page

# switch to 2nd frame
driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,"WebDriver").click()
driver.switch_to.default_content()  # go back to main page

# switch to 3rd frame
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()