from selenium.webdriver.common.by import By
import conftest
from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.usernameField = (By.ID, "user-name")
        self.passwordField = (By.ID, "password")
        self.loginButton = (By.ID, "login-button")

    def doLogin(self, username, password):
        self.fillField(self.usernameField, username)
        self.fillField(self.passwordField, password)
        self.click(self.loginButton)

