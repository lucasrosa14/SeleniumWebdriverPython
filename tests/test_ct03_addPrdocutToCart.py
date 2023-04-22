import time

import pytest
from selenium.webdriver.common.by import By
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

        #Login
        loginPage.doLogin("standard_user", "secret_sauce")

        #Add Backpack to cart
        homePage.addProductToCart("Sauce Labs Backpack")

        #Check cart
        homePage.accessCart()
        cartPage.checkProductExistsOnCart("Sauce Labs Backpack")

        #Click to back
        cartPage.continueShopping()

        #Add Bike Light to cart
        homePage.addProductToCart("Sauce Labs Bike Light")

        #Check cart 2
        homePage.accessCart()
        cartPage.checkProductExistsOnCart("Sauce Labs Backpack")
        cartPage.checkProductExistsOnCart("Sauce Labs Bike Light")
