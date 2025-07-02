from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistration import AccountRegistration

class Test_001_Account_Registration:
    URL = "https://naveenautomationlabs.com/opencart/"

    def test_account_registration(self,setup):
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()

        # Declare object for homepage
        self.hp=HomePage(self.driver)

        # Call ClickMyAccount method
        self.hp.ClickMyAccount()

        # Call ClickRegister method
        self.hp.ClickRegister()

        # Declare object for AccountRegistration
        self.acc_reg_page=AccountRegistration(self.driver)

        # Call methods from AccountRegistration.py
        self.acc_reg_page.SetFirstName("TEST001")
        self.acc_reg_page.SetLastName("TEST002")
        self.acc_reg_page.SetEmail("test@test123.com")
        self.acc_reg_page.SetTelephone("12456325")
        self.acc_reg_page.SetPassword("abcdefg")
        self.acc_reg_page.SetPasswordConfirm("abcdefg")
        self.acc_reg_page.SetPrivacyPolicy()
        self.acc_reg_page.SetClickContinue()
        self.confirmation_msg = self.acc_reg_page.Get_AccountCreation_Msg()
        if self.confirmation_msg == "Your Account Has Been Created!":
            assert True
        else:
            False