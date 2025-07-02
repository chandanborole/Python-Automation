from selenium.webdriver.common.by import By

class HomePage():
    link_myaccount_xpath = "//a[@title='My Account']"
    link_register_linktext = "Register"
    link_login_linktext = "Login"

    def __init__(self,driver):
        self.driver = driver

    def ClickMyAccount(self):
        self.driver.find_element(By.XPATH, self.link_myaccount_xpath).click()

    def ClickRegister(self):
        self.driver.find_element(By.LINK_TEXT, self.link_register_linktext).click()

    def ClickLogin(self):
        self.driver.find_element(By.LINK_TEXT, self.link_login_linktext).click()

