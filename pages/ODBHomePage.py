from BasePage                           import BasePage, IncorrectPageException
from POMPythonSeleniumWebdriver.Constants                  import TeamOne_Constants
from POMPythonSeleniumWebdriver.UIMaps.GlobalUIMap         import PageTitlesAndURLsMap, ODBHomePageMap #AboutUsPageMap, CareersPageMap, WorkPageMap
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains


class ODBHomePage(BasePage):

    def __init__(self, driver):
        super(ODBHomePage, self).__init__(driver)
        #self.refresh_page()


    def _verify_page(self):
        try:
            self.wait_for_element_visibility(10, "name",
                                             ODBHomePageMap['ODBLoginUsernameName'])
        except:
            raise IncorrectPageException


    def odb_login(self):
        self.find_element("name",ODBHomePageMap['ODBLoginUsernameName']).send_keys("admin")
        self.find_element("name",ODBHomePageMap['ODBLoginPasswordName']).send_keys("admin")
        self.find_element("name",ODBHomePageMap['ODBLoginUsernameName']).submit()

    def odb_click_newslist(self):
        self.find_element("linkText",ODBHomePageMap['ODBNewsListLinkText']).click()

    def odb_search(self):
        self.find_element("id",ODBHomePageMap['ODBSearchID']).clear()
        self.find_element("id",ODBHomePageMap['ODBSearchID']).send_keys("gaza")
        self.click(10,"name",ODBHomePageMap['ODBSearchButtonName'])
        cols = self.find_elements("xpath",ODBHomePageMap['ODBCols'])
        i = 1
        for col in cols:
            print (str(i) + " => " + col.text)
            i = i + 1

    def odb_logout(self):
        ActionChains(self.driver).\
            move_to_element(self.wait_for_element_visibility(10,"id",ODBHomePageMap['ODBAdminDropdownID'])).\
            click().\
            perform()

        ActionChains(self.driver).\
            move_to_element(self.wait_for_element_visibility(10,"xpath",ODBHomePageMap['ODBLogoutButtonXpath'])).\
            click().\
            perform()
        #self.click(10,"xpath",ODBHomePageMap['ODBLogoutButtonXpath'])
        pass