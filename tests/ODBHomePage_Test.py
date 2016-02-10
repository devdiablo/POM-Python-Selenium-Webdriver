from POMPythonSeleniumWebdriver.Constants              import TeamOne_Constants
from POMPythonSeleniumWebdriver.BaseTestCase           import BaseTestCase
from POMPythonSeleniumWebdriver.pages.HomePage         import HomePage
from POMPythonSeleniumWebdriver.pages.GlobalsPage      import GlobalsPage
from POMPythonSeleniumWebdriver.pages.ODBHomePage      import ODBHomePage
import unittest
#from nose.plugins.attrib import attr


class ODBHomePageTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(ODBHomePageTest, self).setUp()
        self.navigate_to_page(TeamOne_Constants['Base_URL'])
        self.ODBHomePage_obj = ODBHomePage(self.driver)
        print "\n"

    def tearDown(self):
        super(ODBHomePageTest, self).tearDown()


    def test_ODBLoginSearch(self):
        print "Launching the ODB Home Page and Verify Search Functionality."
        self.ODBHomePage_obj.odb_login()
        self.ODBHomePage_obj.odb_click_newslist()
        self.ODBHomePage_obj.odb_search()
        self.ODBHomePage_obj.odb_logout()



if __name__ == "__main__":
    unittest.main()


