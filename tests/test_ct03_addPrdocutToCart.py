import pytest

import conftest
from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.addToCart
@pytest.mark.smoke
class TestCT03:
    def test_ct03_addPrdocutToCart(self):
        driver = conftest.driver
        loginPage = LoginPage()
        homePage = HomePage()
        cartPage = CartPage()

        username = "standard_user"
        password = "secret_sauce"
        productOne = "Sauce Labs Backpack"
        productTwo = "Sauce Labs Bike Light"

        # Login
        loginPage.doLogin(username, password)

        # Add Backpack to cart
        homePage.addProductToCart(productOne)

        # Check cart
        homePage.accessCart()
        cartPage.checkProductExistsOnCart(productOne)

        # Click to back
        cartPage.continueShopping()

        # Add Bike Light to cart
        homePage.addProductToCart(productTwo)

        # Check cart 2
        homePage.accessCart()
        cartPage.checkProductExistsOnCart(productOne)
        cartPage.checkProductExistsOnCart(productTwo)
