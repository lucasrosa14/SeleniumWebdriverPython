import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.smoke
class TestCT01:
    def test_ct01_loginSuccessul(self):
        driver = conftest.driver
        loginPage = LoginPage()
        loginPage.doLogin("standard_user", "secret_sauce")
        assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()


