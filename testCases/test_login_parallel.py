import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time

class Test_002__Login_Parallel_Execution:
    baseURL = ReadConfig.getApplicationURL()
    invalid_username = ReadConfig.getInvalidUser()
    invaliduser_pwd = ReadConfig.getInvalidUserPasswd()

    logger = LogGen.loggen()

    # Verify the login Success with Browser1
    def test_login_success_browser1(self,setup):
        self.driver = setup
        self.logger.info("****Started Login Success test ****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(25)
        self.lp = LoginPage(self.driver)
        hrmuser = self.lp.captureUserDetailsElement()
        userElements = hrmuser.split(' ', 8)
        username = userElements[3]
        password = userElements[7]
        self.lp.setUserName(username)
        self.lp.setPassword(password)
        self.lp.clickLogin()
        time.sleep(5)
        get_user = self.lp.getDisplayedUserName()
        self.logger.info("The User Name is "+get_user)
        print(get_user)
        time.sleep(5)
        self.lp.clickOnWelcomeLabel()
        time.sleep(5)
        self.lp.clickLogout()
        self.driver.close()
        self.logger.info("****Ended Login Success test ****")


    def test_login_success_browser2(self, setup):
        self.driver = setup
        self.logger.info("****Started Login Success test ****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(25)
        self.lp = LoginPage(self.driver)
        hrmuser = self.lp.captureUserDetailsElement()
        userElements = hrmuser.split(' ', 8)
        username = userElements[3]
        password = userElements[7]
        self.lp.setUserName(username)
        self.lp.setPassword(password)
        self.lp.clickLogin()
        time.sleep(5)
        get_user = self.lp.getDisplayedUserName()
        self.logger.info("The User Name is " + get_user)
        print(get_user)
        time.sleep(5)
        self.lp.clickOnWelcomeLabel()
        time.sleep(5)
        self.lp.clickLogout()
        self.driver.close()
        self.logger.info("****Ended Login Success test ****")
