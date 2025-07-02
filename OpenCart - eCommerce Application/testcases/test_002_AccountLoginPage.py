from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistration import AccountRegistration
from pageObjects.AccountLogin import AccountLogin
import time

class Test_002_AccountLogin:

    URL = "https://naveenautomationlabs.com/opencart/"

    def test_account_login(self,setup):
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

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

        time.sleep(5)

        self.driver.close()





