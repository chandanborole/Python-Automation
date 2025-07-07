from pageObjects.Changeyourpassword import Changeyourpassword
from pageObjects.Edityouraccountinformation import Edityouraccountinformation
from pageObjects.Modifyyouraddressbookentries import Modifyyouraddressbookentries
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistration import AccountRegistration
from pageObjects.AccountLogin import AccountLogin
from pageObjects.Desktop import Desktop
from selenium.webdriver.support.select import Select
import time

class Test_006_ModifyYourAddressBookEntries:

    URL = "https://naveenautomationlabs.com/opencart/"

    def test_modifyyouraddressbookentries(self,setup):
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
        self.account_login.SetPassword("QATesting@12345")
        self.account_login.ClickLoginButton()

        # Declare object for ModifyYourAddressBookEntries
        self.modifyyouraddressbookentries = Modifyyouraddressbookentries(self.driver)

        # Call methods from ModifyYourAddressBookEntries.py
        self.modifyyouraddressbookentries.ClickModifyYourAddressBookEntries()
        self.modifyyouraddressbookentries.ClickEdit()
        self.modifyyouraddressbookentries.SetFirstName("QA")
        self.modifyyouraddressbookentries.SetLastName("TESTING")
        self.modifyyouraddressbookentries.SetCompany("AUTOMATION")
        self.modifyyouraddressbookentries.SetAddress1("MARIA ROAD")
        self.modifyyouraddressbookentries.SetAddress2("EAST")
        self.modifyyouraddressbookentries.SetCity("WELLINGTON")
        self.modifyyouraddressbookentries.SetPostCode("9876543210")
        self.modifyyouraddressbookentries.SetCountry("India")
        self.modifyyouraddressbookentries.SetRegion("Maharashtra")
        self.modifyyouraddressbookentries.SetDefaultAddress()
        self.modifyyouraddressbookentries.ClickContinueButton()
        self.confirmation_msg = self.modifyyouraddressbookentries.GetSuccessMessage()
        if self.confirmation_msg == "Your address has been successfully updated":
            assert True
        else:
            False