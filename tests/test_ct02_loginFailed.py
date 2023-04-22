import pytest
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.smoke
class TestCT02:
    def test_ct02_loginFailed(self):

        loginPage = LoginPage()

        expectedErrorMessage = "Epic sadface: Username and password do not match any user in this service"
        username = "standard_user"
        password = "secret_"

        loginPage.doLogin(username, password)
        loginPage.checkLoginError()
        loginPage.checkLoginErrorMessage(expectedErrorMessage)






