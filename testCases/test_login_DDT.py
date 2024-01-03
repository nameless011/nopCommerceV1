# setting up xlsUtility to acess excel data in the test
# modifying testcase with necessary prompt to use the excel data



import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login_page
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGEN
from utilities import XlsxUtility


class Test_002_login_DDT():
    baseURL = ReadConfig.getApplicationURL()
    # username = ReadConfig.getuseremail()
    # password = ReadConfig.getpassword()
    logger = LogGEN.loggen()
    path = ".//testData//TESTDATA.xlsx"

    @pytest.mark.sanity
    def test_login_ddt(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login_page(self.driver)


        self.getrow =  XlsxUtility.getrowCount(self.path,"Sheet1")
        print('Number of rows...', self.getrow)
        lst_result = []
        for r in range(2,self.getrow+1):
            self.user = XlsxUtility.readData(self.path, "Sheet1", r, 1)

            self.pswd = XlsxUtility.readData(self.path, "Sheet1", r, 2)

            self.exp_result = XlsxUtility.readData(self.path, "Sheet1", r, 3)

            self.lp.setPassword(self.pswd)
            self.lp.setUserName(self.user)
            self.lp.clickLogin()
            time.sleep(3)

            actual_title = self.driver.title
            expected_tittle = "Dashboard / nopCommerce administration"

            if actual_title == expected_tittle:
                if self.exp_result == "Pass":
                    self.lp.clickLogout()
                    lst_result.append("Pass")

                elif self.exp_result == "Fail":
                    self.lp.clickLogout()
                    lst_result.append("Fail")

            elif actual_title != expected_tittle:
                if self.exp_result == "Pass":
                    lst_result.append("Fail")

                elif self.exp_result == "Fail":
                    lst_result.append("Pass")

        if "Fail" not in lst_result:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

