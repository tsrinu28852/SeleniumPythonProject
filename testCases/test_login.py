import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time

class Test_001_Invalid_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUser()
    password = ReadConfig.getPassword()
    invalid_username = ReadConfig.getInvalidUser()

    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.driver.get(self.baseURL)
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

    def test_login_success(self,setup):
        self.driver = setup
        self.logger.info("****Started Login Success test ****")
        self.driver.get(self.baseURL)
        time.sleep(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        get_user = self.lp.getDisplayedUserName()
        self.logger.info("The User Name is "+get_user)
        print(get_user)
        time.sleep(3)
        self.lp.clickOnWelcomeLabel()
        time.sleep(2)
        self.lp.clickLogout()
        self.driver.close()
        self.logger.info("****Ended Login Success test ****")

    def test_login_Invalid(self,setup):
        self.logger.info("****Started Login Invalid test ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.invalid_username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        error = self.lp.captureErrorMessage()
        if error == "Invalid credentials" or error =='Credenciales no válidas':
            assert True
        else:
            assert False
        self.driver.close()

    def test_capture_screenshot_failed(self, setup):
        self.logger.info("****Capture screenshot test when test failed ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(10)
        act_title = self.driver.title
        if act_title == "OrangeHRM1":
            self.driver.close()
            assert True
        else:
            self.logger.info("****Captured screenshot****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False





