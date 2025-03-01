from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# execute_script is method

# 1. Scroll down page by pixel
# JavaScript builtin function - "window.scrollBy(0,3000)",""
# 0 = startpoint , 3000 = endpoint & "" should blank
driver.execute_script("window.scrollBy(0,3000)","")
# Shows position of scroll
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value) # ans - 3000

# 2. Scroll down page till the element is visible
flag=driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
# JavaScript builtin function - "arguments[0].scrollIntoView()",""
driver.execute_script("arguments[0].scrollIntoView();",flag)
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value) # ans - 5038.3330078125

# 3. Scroll down page till end
# JavaScript builtin function - "window.scrollBy(0,document.body.scrollHeight)"
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value) # ans - 5990.8330078125

# 4. Scroll up to starting position
# JavaScript builtin function - "window.scrollBy(0,-document.body.scrollHeight)"
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value) # ans - 0