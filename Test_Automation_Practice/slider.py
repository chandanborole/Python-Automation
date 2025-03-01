from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

# Get slider element position
min_slider=driver.find_element(By.XPATH,"//body//div//span[1]")
max_slider=driver.find_element(By.XPATH,"//body//div//span[2]")

print("Location of sliders Before moving........")

# Current slider position
print(min_slider.location) #    {'x': 59, 'y': 252}
print(max_slider.location) #    {'x': 639, 'y': 252}

# Declare ActionChains class . syntax - double_click(element)
act=ActionChains(driver)

# drag_and_drop_by_offset is method
# syntax - drag_and_drop_by_offset(element,X,Y)
# X , Y represent - how much value you have to increase
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-39,0).perform()

print("Location of sliders After moving........")
print(min_slider.location) # {'x': 158, 'y': 252}
print(max_slider.location) # {'x': 598, 'y': 252}