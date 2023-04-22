import pytest
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT02:
    def test_ct02_loginFailed(self):
        expectedErrorMessage = "Epic sadface: Username and password do not match any user in this service"

        loginPage = LoginPage()
        loginPage.doLogin("standard_user", "secret_")
        loginPage.checkLoginError()
        loginPage.checkLoginErrorMessage(expectedErrorMessage)






