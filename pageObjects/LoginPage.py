

class LoginPage:
    # Login Page
    textbox_username_id = "txtUsername"
    textbox_password_id = "txtPassword"
    button_login_id = "btnLogin"
    label_text_id = "welcome"
    link_logout_xpath = "//a[text()='Logout' or text()='Cerrar sesión']"
    error_message_text_xpath = "//span[@id='spanMessage']"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.button_login_id).click()

    def page_has_loaded(self):
        self.log.info("Checking if {} page is loaded.".format(self.driver.current_url))
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'

    def clickOnWelcomeLabel(self):
        self.driver.find_element_by_id(self.label_text_id).click()

    def getDisplayedUserName(self):
        userName = self.driver.find_element_by_id(self.label_text_id).text
        return userName

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.link_logout_xpath).click()

    def captureErrorMessage(self):
        errorMessage= self.driver.find_element_by_xpath(self.error_message_text_xpath).text
        return errorMessage

