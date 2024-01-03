import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login_page
from pageObjects.nopCom_1Page import nopcom_1page
from pageObjects.nopCom_addCustomerPage import nopcom_addCustomer
from utilities.readProperties import ReadConfig
from utilities import generators
from utilities import XlsxUtility
from utilities.customLogger import LogGEN
import os

class Test_addCustomer():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getuseremail()
    password = ReadConfig.getpassword()
    path = ".//testData//TESTDATA.xlsx"
    logger = LogGEN.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self,setup):
        self.logger.info('---------TestCase addCustomer----------------')
        self.driver = setup          #here it is getting the driver from setup method
        self.driver.get(self.baseURL) #mentined inside conftest
        self.lp = Login_page(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('-----------Login Successful----------------')
        time.sleep(3)

        self.nCpage = nopcom_1page(self.driver)
        self.nCpage.goto_Customer()
        time.sleep(1)
        self.nCpage.goto_Customer2()

        self.addcust = nopcom_addCustomer(self.driver)
        self.addcust.clickonAddnew()
        self.logger.info('-----------Adding Customer----------------')

        time.sleep(2)
        self.email = generators.random_generator() + '@gmail.com'
        self.addcust.setEmail(self.email)
        #time.sleep(2)
        self.password = generators.random_num_generator()
        self.addcust.setPassword(self.password)
        #time.sleep(2)
        self.firstname = generators.random_string_generator()
        self.addcust.setFirstname(self.firstname)
        #time.sleep(2)
        self.lname = 'Orton'
        self.addcust.setLastname(self.lname)
        #time.sleep(2)
        self.dobval = "5/20/1997"
        self.addcust.setDob(self.dobval)
        #time.sleep(2)
        self.addcust.setGender('Male')

        self.row = 6
        self.cr = "Administrators"
        self.addcust.setCustomerRole(self.cr)
        self.vendorid = "Vendor 1"
        if self.cr == "Vendors":
            self.addcust.clickVendormanager(self.vendorid)
            XlsxUtility.writeData(self.path, "Sheet2", self.row, 7, data=self.vendorid)
        else:
            XlsxUtility.writeData(self.path, "Sheet2", self.row, 7, data="NA")
        time.sleep(2)
        self.addcust.clickonSave()
        self.logger.info('-----------Saving Customer data----------------')


        XlsxUtility.writeData(self.path,"Sheet2",self.row,1,data=self.email)
        XlsxUtility.writeData(self.path, "Sheet2", self.row, 2, data=self.password)
        XlsxUtility.writeData(self.path, "Sheet2", self.row, 3, data=self.firstname)
        XlsxUtility.writeData(self.path, "Sheet2", self.row, 4, data=self.lname)
        XlsxUtility.writeData(self.path, "Sheet2", self.row, 5, data=self.dobval)
        XlsxUtility.writeData(self.path, "Sheet2", self.row, 6, data=self.cr)
        time.sleep(2)
        self.logger.info('-----------Test data saved in Excel----------------')

        self.pagealert = self.addcust.checkcustomer()
        if 'customer has been added successfully.' in self.pagealert :
            self.logger.info('-----------Saving Customer data Passed----------------')
            self.driver.save_screenshot(".\\screenshots\\" + "test_addcustomerpass.png")
            XlsxUtility.writeData(self.path, "Sheet2", self.row, 8, data="pass")
            assert True
            self.driver.close()
        else:
            self.logger.info('-----------Saving Customer data Failed----------------')
            self.driver.save_screenshot(".\\screenshots\\" + "test_addcustomerfail.png")
            self.driver.close()
            assert False

        self.logger.info('-----------Closing Test----------------')


