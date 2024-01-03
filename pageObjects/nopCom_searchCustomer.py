import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageObjects.BasePage import basepage

class nopCom_searchCustomer(basepage):
    txtEmail_xpah = (By.XPATH,"//input[@id='SearchEmail']")
    txtFirstname_xpath = (By.XPATH,"//input[@id='SearchFirstName']")
    txtLastname_xpath = (By.XPATH,"//input[@id='SearchLastName']")
    butnSearch_xpath = (By.XPATH,"//button[@id='search-customers']")
    tblSearchresult_xpath = (By.XPATH,'//*[@id="customers-grid"]/tbody//td')
    tblrows_xpath = (By.XPATH,'//*[@id="customers-grid"]/tbody//tr')
    tblcolm_xpath = (By.XPATH,'//*[@id="customers-grid"]/tbody//tr')

    def setEmail(self,email):
        self.driver.find_element(*self.txtEmail_xpah).send_keys(email)

    def setFirstname(self,firstname):
        self.driver.find_element(*self.txtFirstname_xpath).send_keys(firstname)

    def setLastname(self,lastname):
        self.driver.find_element(*self.txtLastname_xpath).send_keys(lastname)

    def clickSearchbutton(self):
        self.driver.find_element(*self.butnSearch_xpath).click()

    def getNoofrows(self):
        return len(self.driver.find_elements(*self.tblrows_xpath))

    def getNoofcolm(self):
        return len(self.driver.find_elements(*self.tblcolm_xpath))

    def SearchCutomerbyname(self,name):
        flag = False
        for r in range(1,self.getNoofrows()+1):
            nm = self.driver.find_element(By.XPATH,'//*[@id="customers-grid"]/tbody//tr["+std(r)+"]//td[3]').text
            if nm == name:
                flag = True
                break
        return flag

    def SearchCustomerbyEmail(self,email):
        flag = False
        for r in range(1,self.getNoofrows()+1):
            eml = self.driver.find_element(By.XPATH,'//*[@id="customers-grid"]/tbody//tr["+str(r)+"]//td[2]').text
            if eml == email:
                flag = True
                break
        return flag