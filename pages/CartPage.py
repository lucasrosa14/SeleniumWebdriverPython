from selenium.webdriver.common.by import By
import conftest
from pages.BasePage import BasePage


class CartPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.inventoryItem = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.continueShoppingButton = (By.ID, "continue-shopping")
        self.checkoutButton = (By.ID, "checkout")

    def checkProductExistsOnCart(self, itemName):
        item = (self.inventoryItem[0], self.inventoryItem[1].format(itemName))
        self.checkIfExists(item)

    def continueShopping(self):
        self.click(self.continueShoppingButton)

    def proceedToCheckout(self):
        self.click(self.checkoutButton)
