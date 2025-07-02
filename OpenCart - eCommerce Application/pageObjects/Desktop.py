from selenium.webdriver.common.by import By

class Desktop():
    # Locators Declaration
    # Note - Element declaration syntax
    # textbox_firstname_xpath - element type_what kind of element_used locator)
    dropdowntoggle_desktop_xpath = "//*[@id='menu']/div[2]/ul/li[1]/a"
    dropdowntoggle_pc_xpath = "//*[@id='menu']/div[2]/ul/li[1]/div/div/ul/li[1]/a"
    button_pc_continue_class = "//a[@class='btn btn-primary']"
    featured_macBook_linktext = "MacBook"
    button_addtocart_xpath = "//button[@id='button-cart']"
    success_message_xpath =  "//div[@class='alert alert-success alert-dismissible']"

    # Constructor Declaration
    def __init__(self,driver):
        self.driver = driver

    # Action methods
    def ClickDesktop(self):
        self.driver.find_element(By.XPATH, self.dropdowntoggle_desktop_xpath).click()

    def ClickPC(self):
        self.driver.find_element(By.XPATH, self.dropdowntoggle_pc_xpath).click()

    def ClickContinue(self):
        self.driver.find_element(By.XPATH, self.button_pc_continue_class).click()

    def ClickMacBook(self):
        self.driver.find_element(By.LINK_TEXT, self.featured_macBook_linktext).click()

    def AddToCart(self):
        self.driver.find_element(By.XPATH, self.button_addtocart_xpath).click()

    def SuccessMessage(self):
        self.driver.find_element(By.XPATH, self.success_message_xpath)