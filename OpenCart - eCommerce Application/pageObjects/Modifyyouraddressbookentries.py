from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

class Modifyyouraddressbookentries():
    # Locators Declaration
    # Note - Element declaration syntax
    # textbox_firstname_xpath - element type_what kind of element_used locator)
    click_modifyyouraddressbookentries_xpath = "//*[@id='content']/ul[1]/li[3]/a"
    button_clickedit_xpath = "//*[@id='content']/div[1]/table/tbody/tr/td[2]/a[1]"
    textbox_firstname_xpath = "//input[@id='input-firstname']"
    textbox_lastname_xpath = "//input[@id='input-lastname']"
    textbox_company_xpath = "//input[@name='company']"
    textbox_address1_xpath = "//input[@type='text' and @name='address_1']"
    textbox_address2_xpath = "//input[@type='text' and @name='address_2']"
    textbox_city_xpath = "//input[@type='text' and @name='city']"
    textbox_postcode_xpath = "//input[@type='text' and @name='postcode']"
    dropdown_country_xpath = "//select[@id='input-country']"
    dropdown_region_xpath = "//select[@id='input-zone']"
    radiobutton_defaultaddress_xpath = "//input[@type='radio' and @value='1']"
    button_continue_xpath = "//input[@type='submit' and @class='btn btn-primary']"
    success_verificationmessage_xpath = "//*[@id='account-address']/div[1]"

    # Constructor declaration
    def __init__(self,driver):
        self.driver = driver

    # Action methods
    def ClickModifyYourAddressBookEntries(self):
        self.driver.find_element(By.XPATH, self.click_modifyyouraddressbookentries_xpath).click()

    def ClickEdit(self):
        clickedit = self.driver.find_element(By.XPATH, self.button_clickedit_xpath)
        clickedit.click()

    def SetFirstName(self,firstname):
        setfirstname = self.driver.find_element(By.XPATH, self.textbox_firstname_xpath)
        setfirstname.clear()
        setfirstname.send_keys(firstname)

    def SetLastName(self,lastname):
        setlastname = self.driver.find_element(By.XPATH, self.textbox_lastname_xpath)
        setlastname.clear()
        setlastname.send_keys(lastname)

    def SetCompany(self,company):
        setcompany = self.driver.find_element(By.XPATH, self.textbox_company_xpath)
        setcompany.clear()
        setcompany.send_keys(company)

    def SetAddress1(self,address1):
        setaddress1 = self.driver.find_element(By.XPATH, self.textbox_address1_xpath)
        setaddress1.clear()
        setaddress1.send_keys(address1)

    def SetAddress2(self,address2):
        setaddress2 = self.driver.find_element(By.XPATH, self.textbox_address2_xpath)
        setaddress2.clear()
        setaddress2.send_keys(address2)

    def SetCity(self,city):
        setcity = self.driver.find_element(By.XPATH, self.textbox_city_xpath)
        setcity.clear()
        setcity.send_keys(city)

    def SetPostCode(self,postcode):
        setpostcode = self.driver.find_element(By.XPATH, self.textbox_postcode_xpath)
        setpostcode.clear()
        setpostcode.send_keys(postcode)

    def SetCountry(self,country):
        setcountry = Select(self.driver.find_element(By.XPATH, self.dropdown_country_xpath))
        setcountry.select_by_visible_text(country)

    def SetRegion(self,region):
        setregion = Select(self.driver.find_element(By.XPATH, self.dropdown_region_xpath))
        setregion.select_by_visible_text(region)

    def SetDefaultAddress(self):
        setdefaultaddress = self.driver.find_element(By.XPATH, self.radiobutton_defaultaddress_xpath)
        setdefaultaddress.click()

    def ClickContinueButton(self):
        clickcontinuebutton = self.driver.find_element(By.XPATH, self.button_continue_xpath)
        clickcontinuebutton.click()

    def GetSuccessMessage(self):
        try:
            return self.driver.find_element(By.XPATH, self.success_verificationmessage_xpath)
        except:
            None

    time.sleep(5)