from selenium.webdriver.common.by import By

class Changeyourpassword():
    # Locators Declaration
    # Note - Element declaration syntax
    # textbox_firstname_xpath - element type_what kind of element_used locator)
    #click_changeyourpassword_xpath = "//*[@id='content]/ul[1]/li[2]/a"
    click_changeyourpassword_xpath = "//a[normalize-space()='Change your password']"
    textbox_fillpassword_xpath = "//input[@id='input-password']"
    textbox_fillconfirmpassword_xpath = "//input[@id='input-confirm']"
    button_continue_xpath = "//input[@value='Continue']"
    success_verificationmessage_xpath = "//div[@class='alert alert-success alert-dismissible']"

    # Constructor declaration
    def __init__(self, driver):
        self.driver = driver

    # Action methods
    def Click_ChangeYourPassword(self):
        changepassword = self.driver.find_element(By.XPATH, self.click_changeyourpassword_xpath)
        changepassword.click()

    def SetPassword(self,password):
        setpasword = self.driver.find_element(By.XPATH, self.textbox_fillpassword_xpath)
        setpasword.send_keys(password)

    def SetConfirmPassword(self,confirmpassword):
        setconfirmpassword = self.driver.find_element(By.XPATH, self.textbox_fillconfirmpassword_xpath)
        setconfirmpassword.send_keys(confirmpassword)

    def ClickContinue(self):
        clickcontinue = self.driver.find_element(By.XPATH, self.button_continue_xpath)
        clickcontinue.click()

    def GetSuccessMessage(self):
        try:
            return self.driver.find_element(By.XPATH, self.success_verificationmessage_xpath)
        except:
            None



