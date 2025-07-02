from pageObjects.Edityouraccountinformation import Edityouraccountinformation
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistration import AccountRegistration
from pageObjects.AccountLogin import AccountLogin
from pageObjects.Desktop import Desktop
import time

class Test_004_EditYourAccountInformation:

    URL = "https://naveenautomationlabs.com/opencart/"

    def test_edityouraccountinformation(self,setup):
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
        self.account_login.SetEmail("sadasdsa@fgd.com")
        self.account_login.SetPassword("sadsadsad@123")
        self.account_login.ClickLoginButton()

        # Declare object for EditYourAccountInformation
        self.edityouraccountinformation = Edityouraccountinformation(self.driver)

        # Call methods from EditYourAccountInformation.py
        self.edityouraccountinformation.Click_EditYourAccountInformation()
        self.edityouraccountinformation.SetFirstaName("QATesting")
        self.edityouraccountinformation.SetLastName("Automation")
        self.edityouraccountinformation.SetEmail("qaautomation@automaiton.com")
        self.edityouraccountinformation.SetTelephone("7412589630")
        self.edityouraccountinformation.ClickContinueButton()
        self.confirmation_msg = self.edityouraccountinformation.GetSuccessMessage()
        if self.confirmation_msg == "Success: Your account has been successfully updated.":
            assert True
        else:
            False