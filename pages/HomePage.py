from selenium.webdriver.common.by import By
import conftest
from pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.pageTitle = (By.XPATH, "//span[@class='title']")

    def checkLoginSuccessful(self):
        self.checkIfExists(self.pageTitle)

