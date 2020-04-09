from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
from selenium.webdriver.support.select import Select


class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _searchBar = "//input[@id='search-courses']"
    _searchBtn = '//*[@id="search-course-button"]/i'
    _course = "//div[contains(text(),'{0}')]"
    _enroll = "//button[@id='enroll-button-top']"
    _dropdownPayment = "//button[@class='dropbtn minimal']"
    _cardNumber = "//span[@class='InputContainer']//input[@name='cardnumber']"
    _expDate = "//span[@class='InputContainer']//input[@name='exp-date']"
    _cvc = "//span[@class='InputContainer']//input[@name='cvc']"
    _country = "//select[@id='country_code_credit_card-cc']"
    _zip = "//span[@class='InputContainer']//input[@name='postal']"
    _acceptPolicy = "//input[@id='agreed_to_terms_checkbox']"
    _enrollCourse = "//button[@id='confirm-purchase']"
    _scrollTo = "//h2[contains(text(),'Payment Information')]"
    # _errorMsg = "//button[@id='confirm-purchase']/label"

    def searchBarSendKeys(self, data):
        self.sendKeys(data, self._searchBar, 'xpath')
        self.elementClick(self._searchBtn,'xpath')

    def selectCourse(self, fullCourseName):
        self.elementClick(self._course.format(fullCourseName), 'xpath')

    def clickEnrollBtn(self):
        self.elementClick(self._enroll, 'xpath')

    # def selectPayment(self, data):
    #     self.switchToFrame(name='')
    #     sel = Select(self.getElement(self._dropdownPayment, 'xpath'))
    #     sel.select_by_index(data)
    #     self.switchToDefaultContent()

    def sendCardNumber(self, data):
        self.switchToFrame(name='__privateStripeFrame8')
        self.sendKeys(data, self._cardNumber, 'xpath')
        self.switchToDefaultContent()
    def sendExpDate(self, data):
        self.switchToFrame(name='__privateStripeFrame9')
        self.sendKeys(data, self._expDate, 'xpath')
        self.switchToDefaultContent()

    def sendCvc(self, data):
        self.switchToFrame(name='__privateStripeFrame10')
        self.sendKeys(data, self._cvc, 'xpath')
        self.switchToDefaultContent()

    def selectCountry(self, data):
        sel = Select(self.getElement(self._country, 'xpath'))
        sel.select_by_visible_text(data)


    def sendZip(self, data):
        self.switchToFrame(name='__privateStripeFrame11')
        self.sendKeys(data, self._zip, 'xpath')
        self.switchToDefaultContent()

    def clickPolicy(self):
        self.elementClick(self._acceptPolicy, 'xpath')

    # def clickEnrollCourse(self):
    #     self.elementClick(self._enrollCourse, 'xpath')

    def enterCardInfo(self, credit,expDate, cvc, country, zip):
        self.scrollToElement(self._scrollTo, 'xpath')
        self.sendCardNumber(credit)
        self.sendExpDate(expDate)
        self.sendCvc(cvc)
        self.selectCountry(country)
        self.sendZip(zip)

    def enrollToCourse(self, courseName, fullCourseName):
        self.searchBarSendKeys(courseName)
        self.selectCourse(fullCourseName)
        self.clickEnrollBtn()
        self.enterCardInfo('1054', '1022', '333', 'Serbia','55555')
        self.clickPolicy()
        # self.clickEnrollCourse()

    # def verifyEnrollFailed(self):
    #     element = self.waitForElement(self._errorMsg, 'xpath')
    #     result = self.isElementDisplayed(element=element)
    #     return result

    def verifyIfEnrollBtnIsDisable(self):
        result = self.isEnabled(self._enrollCourse,'xpath', 'Verification of Enroll Button')
        return not result
