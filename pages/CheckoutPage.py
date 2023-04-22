from selenium.webdriver.common.by import By

import conftest
from pages.BasePage import BasePage


class CheckoutPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver

        self.firstNameField = (By.ID, "first-name")
        self.lastNameField = (By.ID, "last-name")
        self.postalCodeField = (By.ID, "postal-code")
        self.continueButton = (By.ID, "continue")

    def fillShippingInformation(self, firstName, lastName, postalCode):
        self.fillField(self.firstNameField, firstName)
        self.fillField(self.lastNameField, lastName)
        self.fillField(self.postalCodeField, postalCode)

    def clickContinueButton(self):
        self.click(self.continueButton)
