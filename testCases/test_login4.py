# setting up customLogger inside  utilites to generate Logs inside Logs file
# modifyting testCase with necessary log prompt


import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login_page
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGEN
import os

class Test_001_Login():

    baseURL = ReadConfig.getApplicationURL() # getting url from .ini file
    username = ReadConfig.getuseremail() #getting email from .ini file
    password = ReadConfig.getpassword()  #getting password from .ini file

    logger1 = LogGEN.loggen()   #creating logger object

    @pytest.mark.regression
    def test_homePageTittle(self,setup):
        self.logger1.info("---------------Test Starting------------")
        self.driver = setup
        self.driver.get(self.baseURL)
        page_tittle = self.driver.title
        if page_tittle == "Your store. Login":
            self.logger1.debug("************Test is passed***********")
            assert True
            self.driver.close()
        else:
            self.logger1.debug("************Test is failed************")
            self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTittle.png")
            #self.driver.save_screenshot(os.path.abspath(os.curdir)+".\\screenshots\\"+"test_homePageTittle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):   #setup needs to be mentioned here
        self.driver = setup          #here it is getting the driver from setup method
        self.driver.get(self.baseURL) #mentined inside conftest
        self.lp = Login_page(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        page_tittle = self.driver.title
        self.lp.clickLogout()
        time.sleep(2)
        if page_tittle == "Dashboard / nopCommerce administration": #purposefully given wrong
            self.logger1.debug("************Test is passed***********")
            assert True                                             #replaced / with,
            self.driver.close()
        else:
            self.logger1.error("************Test is failed***********")
            self.driver.save_screenshot(".\\screenshots\\"+"test_login.png")
            #self.driver.save_screenshot(os.path.abspath(os.curdir)+".\\screenshots\\"+"test_login.png")
            self.driver.close()
            assert False

