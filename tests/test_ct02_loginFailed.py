import pytest
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT02:
    def test_ct02_loginFailed(self):
        loginPage = LoginPage()
        loginPage.doLogin("standard_user", "secret_")
        loginPage.checkLoginError()






