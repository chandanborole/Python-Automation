from selenium.webdriver.common.by import By

class AccountRegistration():
    # Locators Declaration
    # Note - Element declaration syntax
    # textbox_firstname_xpath - element type_what kind of element_used locator)
    textbox_firstname_xpath = "//input[@id='input-firstname']"
    textbox_lastname_xpath = "//input[@id='input-lastname']"
    textbox_email_xpath = "//input[@name='email']"
    textbox_telephone_name = 'telephone'
    textbox_password_name = 'password'
    textbox_passwordconfirm_name = 'confirm'
    checkbox_privacypolicy_name = 'agree'
    button_clickcontinue_xpath = "//input[@value='Continue']"
    successmessage_accountcreation_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    # Constructor Declaration
    def __init__(self,driver):
        self.driver = driver

    # Action methods
    def SetFirstName(self,firstname):
        self.driver.find_element(By.XPATH, self.textbox_firstname_xpath).send_keys(firstname)

    def SetLastName(self,lastname):
        self.driver.find_element(By.XPATH, self.textbox_lastname_xpath).send_keys(lastname)

    def SetEmail(self,email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def SetTelephone(self,telephone):
        self.driver.find_element(By.NAME, self.textbox_telephone_name).send_keys(telephone)

    def SetPassword(self,password):
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def SetPasswordConfirm(self,passwordconfirm):
        self.driver.find_element(By.NAME, self.textbox_passwordconfirm_name).send_keys(passwordconfirm)

    def SetPrivacyPolicy(self):
        self.driver.find_element(By.NAME, self.checkbox_privacypolicy_name).click()

    def SetClickContinue(self):
        self.driver.find_element(By.XPATH, self.button_clickcontinue_xpath).click()

    def Get_AccountCreation_Msg(self):
        try:
            return self.driver.find_element(By.XPATH, self.successmessage_accountcreation_xpath).text
        except:
            None