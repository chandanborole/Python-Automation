from selenium.webdriver.common.by import By

class AccountLogin():
    # Locators Declaration
    # Note - Element declaration syntax
    # textbox_firstname_xpath - element type_what kind of element_used locator)
    textbox_email_xpath = "// input[ @ id = 'input-email']"
    textbox_password_xpath = "//input[@id='input-password']"
    button_login_xpath = "//input[@type='submit']"

    # Constructor Declaration
    def __init__(self,driver):
        self.driver = driver

    # Action methods
    def SetEmail(self,email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def SetPassword(self,password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def ClickLoginButton(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()