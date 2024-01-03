import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login_page
from pageObjects.nopCom_1Page import nopcom_1page
from pageObjects.nopCom_searchCustomer import nopCom_searchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGEN
from utilities import XlsxUtility


class Test_searchCustomerbyEmail__008():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getuseremail()
    password = ReadConfig.getpassword()
    logger = LogGEN.loggen()

    @pytest.mark.regression
    def test_searchcustomerbyemail(self,setup):
        self.logger.info("***************   Test_searchCustomerbyEmail__008 Starting     ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login_page(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('-----------   Login Successful    ----------------')
        time.sleep(2)

        self.nCpage = nopcom_1page(self.driver)
        self.nCpage.goto_Customer()
        time.sleep(1)
        self.nCpage.goto_Customer2()
        self.logger.info('-----------   On the Search page  ----------------')

        self.logger.info('-----------   Searching customer by Name    ----------------')
        self.npSearchCust = nopCom_searchCustomer(self.driver)
        self.npSearchCust.setEmail('arthur_holmes@nopCommerce.com')
        self.npSearchCust.clickSearchbutton()
        self.logger.info('-----------Checking customer details on the search table----------------')
        time.sleep(2)
        status = self.npSearchCust.SearchCustomerbyEmail("arthur_holmes@nopCommerce.com")
        self.driver.close()
        assert True == status
        self.logger.info("***************  Test_searchCustomerbyEmail__008 Passed  *********** ")
        self.logger.info("***************  Test_searchCustomerbyEmail__008 Finished  *********** ")

