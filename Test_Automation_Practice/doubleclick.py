from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

# Declare wait
driver.implicitly_wait(10)

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

# Switch to frame
driver.switch_to.frame("iframeResult") # switch to frame

# Fill data in input box
field1=driver.find_element(By.XPATH,"//input[@id='field1']")
field1.clear()
field1.send_keys("welcome")

# Copy text button element
button=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

# Declare ActionChains class . syntax - double_click(element)
act=ActionChains(driver)

# double_click operation
# double_click is method use for double_click on element . syntax - double_click(element) , perform is method
act.double_click(button).perform()



