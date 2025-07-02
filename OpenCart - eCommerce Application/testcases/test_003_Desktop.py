from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistration import AccountRegistration
from pageObjects.AccountLogin import AccountLogin
from pageObjects.Desktop import Desktop
import time

class Test_003_Desktop:

    URL = "https://naveenautomationlabs.com/opencart/"

    def test_click_desktop(self,setup):
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

    # Declare object for Desktop
        self.click_desktop = Desktop(self.driver)

    # Call methods from Desktop.py
        self.click_desktop.ClickDesktop()
        self.click_desktop.ClickPC()
        self.click_desktop.ClickContinue()
        self.click_desktop.ClickMacBook()
        self.click_desktop.AddToCart()

    # Success Message verification
        Success_Message = self.click_desktop.SuccessMessage()
        if Success_Message == self.click_desktop.SuccessMessage:
            print("Success: You have added MacBook to your shopping cart!")
        else:
            print("FAIL")

        time.sleep(5)

        self.driver.close()