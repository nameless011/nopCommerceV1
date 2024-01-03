import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageObjects.BasePage import basepage


class nopcom_addCustomer(basepage):
    butnAddnew_xpath = (By.XPATH,"//a[normalize-space()='Add new']")
    txtEmail_xpath = (By.XPATH,"//input[@id='Email']")
    txtPassword_xpath = (By.XPATH,"//input[@id='Password']")
    txtFirstname_xpath = (By.XPATH,"//input[@id='FirstName']")
    txtLastname_xpath = (By.XPATH,"//input[@id='LastName']")
    rbGendermale_xpath = (By.XPATH,"//input[@id='Gender_Male']")
    rbGenderfemale_xpath = (By.XPATH,"//input[@id='Gender_Female']")
    txtDOB_xpath = (By.XPATH,"//input[@id='DateOfBirth']")
    lstCustomerrole_xpath = (By.XPATH,'//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div')
    lstitemRegistered_xpath = (By.XPATH,"//span[normalize-space()='Registered']")
    lstitemAdministrators_xpath = (By.XPATH,"//li[normalize-space()='Administrators']")
    lstitemForumModerators_xpath = (By.XPATH,"//li[normalize-space()='Forum Moderators']")
    lstitemGuests_xpath = (By.XPATH,"//li[normalize-space()='Guests']")
    lstitemVendors_xpath = (By.XPATH,"//li[contains(text(),'Vendors')]")
    butnRegistereddlt_xpath = (By.XPATH,"//span[@title='delete']")
    drpmgrofVendor_xpath = (By.XPATH,"//select[@id='VendorId']")
    butnSave_xpath = (By.XPATH,"//button[@name='save']")
    alertmsg_xpath = (By.XPATH,"//div[@class='alert alert-success alert-dismissable']")

    def clickonAddnew(self):
        self.driver.find_element(*self.butnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(*self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(*self.txtPassword_xpath).send_keys(password)

    def setFirstname(self,firstname):
        self.driver.find_element(*self.txtFirstname_xpath).send_keys(firstname)

    def setLastname(self,lastname):
        self.driver.find_element(*self.txtLastname_xpath).send_keys(lastname)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element(*self.rbGendermale_xpath).click()
        elif gender == "Female":
            self.driver.find_element(*self.rbGenderfemale_xpath).click()
        else:
            self.driver.find_element(*self.rbGendermale_xpath).click()

    def setDob(self,dob):
        self.driver.find_element(*self.txtDOB_xpath).send_keys(dob)

    def setCustomerRole(self,role):
        self.driver.find_element(*self.lstCustomerrole_xpath).click()
        time.sleep(2)
        if role == "Registered":
            time.sleep(1)
            self.driver.find_element(*self.lstitemRegistered_xpath).click()
        elif role == 'Administrators':
            time.sleep(1)
            self.driver.find_element(*self.lstitemAdministrators_xpath).click()
        elif role == "Forum Moderators":
            time.sleep(1)
            self.driver.find_element(*self.lstitemForumModerators_xpath).click()
        elif role == "Vendors":
            time.sleep(1)
            self.driver.find_element(*self.lstitemVendors_xpath).click()
        elif role == "Guests":
            time.sleep(1)
            self.driver.find_element(*self.butnRegistereddlt_xpath).click()
            self.driver.find_element(*self.lstitemGuests_xpath).click()
        else:
            pass

        # self.driver.execute_script("arguments[0].click();", self.lst)
        # self.driver.execute_script("arguments[0].click();", self.lstitm)
    def clickVendormanager(self,vendor):
        drpdown = Select(self.driver.find_element(*self.drpmgrofVendor_xpath))
        drpdown.select_by_visible_text(vendor)
    def clickonSave(self):
        self.driver.find_element(*self.butnSave_xpath).click()

    def checkcustomer(self):
        self.pagemsg = self.driver.find_element(*self.alertmsg_xpath)
        return self.pagemsg.text
