import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time

class Test_001__Login:
    baseURL = ReadConfig.getApplicationURL()
    invalid_username = ReadConfig.getInvalidUser()
    invaliduser_pwd = ReadConfig.getInvalidUserPasswd()

    logger = LogGen.loggen()

    # Verify the Title
    def test_homePageTitle(self,setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(10)
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.close()
            assert False

    # Verify the login Success
    def test_login_success(self,setup):
        self.driver = setup
        self.logger.info("****Started Login Success test ****")
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(25)
        self.lp = LoginPage(self.driver)
        #Capture User Credentials
        hrmuser = self.lp.captureUserDetailsElement()
        userElements = hrmuser.split(' ', 8)
        #Capture username
        username = userElements[3]
        #Capture Password
        password = userElements[7]
        self.lp.setUserName(username)
        self.lp.setPassword(password)
        self.lp.clickLogin()
        time.sleep(5)
        get_user = self.lp.getDisplayedUserName()
        self.logger.info("******* Capture Logged User as Admin User ****")
        self.logger.info("The User Name is "+get_user)
        self.logger.info("########## UserName is Captured  ####################")
        print(get_user)
        time.sleep(5)
        self.lp.clickOnWelcomeLabel()
        time.sleep(5)
        self.lp.clickLogout()
        self.driver.close()
        self.logger.info("****Ended Login Success test ****")

    # Verify the Error Message for Invalid Credentials
    def test_login_Invalid(self,setup):
        self.logger.info("****Started Login Invalid test ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(25)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.invalid_username)
        self.lp.setPassword(self.invaliduser_pwd)
        self.lp.clickLogin()
        time.sleep(5)
        error = self.lp.captureErrorMessage()
        if error == "Invalid credentials" or error =='Credenciales no válidas':
            self.logger.info("****Verified and matched Error Message for Invalid credentials****")
            assert True
        else:
            assert False
            self.logger.info("****Verified and not matched Error Message for Invalid credentials****")
        self.driver.close()

    # Capture Screenshot when Test Case Fails
    def test_capture_screenshot_failed(self, setup):
        self.logger.info("****Capture screenshot test when test failed ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(10)
        act_title = self.driver.title
        if act_title == "OrangeHRM1":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.logger.error("****Captured screenshot****")
            self.driver.close()
            assert False






