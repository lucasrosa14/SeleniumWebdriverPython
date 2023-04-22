import time

import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.PaymentPage import PaymentPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.checkout
@pytest.mark.smoke
class TestCT04:
    def test_ct04_checkoutOneProduct(self):
        loginPage = LoginPage()
        homePage = HomePage()
        cartPage = CartPage()
        checkoutPage = CheckoutPage()
        paymentPage = PaymentPage()

        username = "standard_user"
        password = "secret_sauce"
        firstName = "Lucas"
        lastName = "Rosa"
        postalCode = "88780-000"
        productOne = "Sauce Labs Backpack"
        expectedSuccessfulMessage = "Thank you for your order!"

        #Login
        loginPage.doLogin(username, password)
        homePage.checkLoginSuccessful()

        #Add Backpack to cart
        homePage.addProductToCart(productOne)

        #Check cart
        homePage.accessCart()
        cartPage.checkProductExistsOnCart(productOne)

        #Checkout
        cartPage.proceedToCheckout()
        checkoutPage.fillShippingInformation(firstName, lastName, postalCode)
        checkoutPage.clickContinueButton()
        paymentPage.checkProductExistsPaymentPage(productOne)
        paymentPage.clickFinishButton()
        paymentPage.checkSuccessfulMessage(expectedSuccessfulMessage)


