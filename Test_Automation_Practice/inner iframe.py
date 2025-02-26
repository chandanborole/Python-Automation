from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

# Click iFrame button
driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

# Find outer frame
outerframe = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

# Find inner frame
innerframe = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

# Input text
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("testautomation")

time.sleep(3)