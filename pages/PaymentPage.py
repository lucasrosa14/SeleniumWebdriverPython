from selenium.webdriver.common.by import By
import conftest
from pages.BasePage import BasePage


class PaymentPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver

        self.inventoryItem = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.finishButton = (By.ID, "finish")
        self.thanksMessage = (By.XPATH, "//*[@class='complete-header']")

    def checkProductExistsPaymentPage(self, itemName):
        item = (self.inventoryItem[0], self.inventoryItem[1].format(itemName))
        self.checkIfExists(item)

    def clickFinishButton(self):
        self.click(self.finishButton)

    def checkSuccessfulMessage(self, expectedText):
        foundText = self.getElementText(self.thanksMessage)
        assert foundText == expectedText, f"The returned text was '{foundText}', but the expected text was '{expectedText}'. "



        # assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        # driver.find_element(By.ID, "finish").click()
        # assert driver.find_element(By.XPATH, "//*[@class='complete-header']").is_displayed()