from selenium.webdriver.common.by import By
import conftest
from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.usernameField = (By.ID, "user-name")
        self.passwordField = (By.ID, "password")
        self.loginButton = (By.ID, "login-button")
        self.errorMessageLogin = (By.XPATH, "//*[@data-test='error']")

    def doLogin(self, username, password):
        self.fillField(self.usernameField, username)
        self.fillField(self.passwordField, password)
        self.click(self.loginButton)

        # Login pressing ENTER
        # self.pressKey(self.passwordField, "ENTER")

    def checkLoginError(self):
        self.checkIfExists(self.errorMessageLogin)

    def checkLoginErrorMessage(self, expectedText):
        foundText = self.getElementText(self.errorMessageLogin)
        assert foundText == expectedText, f"The returned text was '{foundText}', but the expected text was '{expectedText}'. "
