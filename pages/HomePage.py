from selenium.webdriver.common.by import By

import conftest
from pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver

        self.pageTitle = (By.XPATH, "//span[@class='title']")
        self.inventoryItem = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.addToCartButton = (By.XPATH, "//*[text()='Add to cart']")
        self.cartButton = (By.XPATH, "//*[@class='shopping_cart_link']")

    def checkLoginSuccessful(self):
        self.checkIfExists(self.pageTitle)

    def addProductToCart(self, itemName):
        item = (self.inventoryItem[0], self.inventoryItem[1].format(itemName))
        self.click(item)
        self.click(self.addToCartButton)

    def accessCart(self):
        self.click(self.cartButton)
