
from selenium.webdriver.common.by import By
from pageObjects.BasePage import basepage

class nopcom_1page(basepage):
    lnkCustomermenu_xpath = (By.XPATH,"//a[@href='#']//p[contains(text(),'Customers')]")
    lnkCustomermenuitem_xpath = (By.XPATH,"/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p")

    def goto_Customer(self):
        self.driver.find_element(*self.lnkCustomermenu_xpath).click()
    def goto_Customer2(self):
        self.driver.find_element(*self.lnkCustomermenuitem_xpath).click()
