from pageObjects.Changeyourpassword import Changeyourpassword
from pageObjects.Edityouraccountinformation import Edityouraccountinformation
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistration import AccountRegistration
from pageObjects.AccountLogin import AccountLogin
from pageObjects.Desktop import Desktop
import time

class Test_005_ChangeYourPassword:

    URL = "https://naveenautomationlabs.com/opencart/"

    def test_changeyourpassword(self,setup):
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Declare object for homepage
        self.hp = HomePage(self.driver)

        # Call ClickMyAccount method from Homepage.py
        self.hp.ClickMyAccount()

        # Call ClickLogin method from Homepage.py
        self.hp.ClickLogin()

        # Declare object for AccountLogin
        self.account_login = AccountLogin(self.driver)

        # Call methods from AccountLogin.py
        self.account_login.SetEmail("qaautomation@automaiton.com")
        self.account_login.SetPassword("Automation@3686")
        self.account_login.ClickLoginButton()

        # Declare object for ChangeYourPassword
        self.changeyourpassword = Changeyourpassword(self.driver)

        # Call methods from EditYourAccountInformation.py
        self.changeyourpassword.Click_ChangeYourPassword()
        self.changeyourpassword.SetPassword("QATesting@12345")
        self.changeyourpassword.SetConfirmPassword("QATesting@12345")
        self.changeyourpassword.ClickContinue()
        self.confirmation_msg = self.changeyourpassword.GetSuccessMessage()
        if self.confirmation_msg == "Success: Your password has been successfully updated.":
            assert True
        else:
            False

        # if self.confirmation_msg != "Success: Your account has been successfully updated.":
        #     assert True
        # else:
        #     False