from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

windowid=driver.current_window_handle
print(windowid)

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowsIDs=driver.window_handles

# Approach1
parentwindowid=windowsIDs[0] #CDwindow-A82AD2C060A4BBCAFAD3DF3C6172CCBE
childwindowid=windowsIDs[1] #CDwindow-F63E2A3D2324F7132FFD60C9A8E16A95
print(parentwindowid,childwindowid)

driver.switch_to.window(childwindowid)
print("title of the child window",driver.title)

driver.switch_to.window(parentwindowid)
print("title of the parent window",driver.title)

#Approach2

for winid in windowsIDs:
    driver.switch_to.window(winid)
    print(driver.title)


#Close specific browser windows   1 2 3
for winid in windowsIDs:
    driver.switch_to.window(winid)
    if driver.title=="OrangeHRM HR Software | Free HR Software | HRMS | HRIS" or driver.title=='XYZ':
        driver.close()