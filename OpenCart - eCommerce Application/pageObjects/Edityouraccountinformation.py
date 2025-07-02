from selenium.webdriver.common.by import By

class Edityouraccountinformation():
    # Locators Declaration
    # Note - Element declaration syntax
    # textbox_firstname_xpath - element type_what kind of element_used locator)
    click_edityouraccountinformation_xpath = "//*[@id='content']/ul[1]/li[1]/a"
    textbox_firstname_xpath = "//input[@id='input-firstname']"
    textbox_lastname_xpath = "//input[@id='input-lastname']"
    textbox_email_xpath = "//input[@id='input-email']"
    textbox_telephone_xpath = "//input[@name='telephone' and @id='input-telephone']"
    button_continue_xpath = "//input[@type='submit' and @value='Continue']"
    success_verificationmessage_xpath = "//div[@class='alert alert-success alert-dismissible']"

    #Constucture declaration
    def __init__(self,driver):
        self.driver = driver

    # Action methods
    def Click_EditYourAccountInformation(self):
        editinfo = self.driver.find_element(By.XPATH, self.click_edityouraccountinformation_xpath)
        editinfo.click()

    def SetFirstaName(self,firstname):
        setfirstname = self.driver.find_element(By.XPATH, self.textbox_firstname_xpath)
        setfirstname.clear()
        setfirstname.send_keys(firstname)

    def SetLastName(self,lastname):
        setlastname = self.driver.find_element(By.XPATH, self.textbox_lastname_xpath)
        setlastname.clear()
        setlastname.send_keys(lastname)

    def SetEmail(self,email):
        setemail = self.driver.find_element(By.XPATH, self.textbox_email_xpath)
        setemail.clear()
        setemail.send_keys(email)

    def SetTelephone(self,telephone):
        settelephone = self.driver.find_element(By.XPATH, self.textbox_telephone_xpath)
        settelephone.clear()
        settelephone.send_keys(telephone)

    def ClickContinueButton(self):
        self.driver.find_element(By.XPATH, self.button_continue_xpath).click

    def GetSuccessMessage(self):
        try:
            return self.driver.find_element(By.XPATH, self.success_verificationmessage_xpath)
        except:
            None