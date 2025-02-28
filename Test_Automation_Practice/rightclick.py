from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

# Declare wait
driver.implicitly_wait(10)

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

# Capture button element
button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

# Declare ActionChains class
act=ActionChains(driver)

# right click operation
# context_click is method use for right click on element . syntax - context_click(element) , perform is method
act.context_click(button).perform()