from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

# Declare wait
driver.implicitly_wait(10)

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

# Drag and Drop elements capture
rome_ele=driver.find_element(By.ID,"box6")
italy_ele=driver.find_element(By.ID,"box106")

# Declare ActionChains class
act=ActionChains(driver)

# drag_and_drop operation
# drag_and_drop is method use for drag_and_drop element . syntax - drag_and_drop(source element , target element) , perform is method
act.drag_and_drop(rome_ele , italy_ele).perform()

wsh_ele=driver.find_element(By.ID,"box3")
italy_ele=driver.find_element(By.ID,"box103")
act.drag_and_drop(wsh_ele,italy_ele).perform()  # drag and drop opration