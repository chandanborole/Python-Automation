from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()

# Login
driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(3)

# Mouse hover on - admin , user management , users
admin=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewAdminModule']/b")
usermgmt=driver.find_element(By.XPATH,"//*[@id='menu_admin_UserManagement']")
users=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']")

# Declare ActionChains class
act=ActionChains(driver)

# mouse hover operation
# move_to_element is method . syntax - move_to_element(element) , perform is method
act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()




