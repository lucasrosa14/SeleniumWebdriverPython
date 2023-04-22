import pytest

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.smoke
class TestCT01:
    def test_ct01_loginSuccessul(self):
        loginPage = LoginPage()
        homePage = HomePage()

        username = "standard_user"
        password = "secret_sauce"

        loginPage.doLogin(username, password)
        homePage.checkLoginSuccessful()
