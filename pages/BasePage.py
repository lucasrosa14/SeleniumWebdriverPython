import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class BasePage:

    def __init__(self):
        self.driver = conftest.driver

    def findElement(self, locator):
        return self.driver.find_element(*locator)

    def findElements(self, locator):
        return self.driver.find_elements(*locator)

    def fillField(self, locator, text):
        self.findElement(locator).send_keys(text)

    def click(self, locator):
        self.findElement(locator).click()

    def checkIfExists(self, locator):
        assert self.findElement(locator).is_displayed(), f"The element '{locator}' is not present in this page."

    def getElementText(self, locator):
        return self.findElement(locator).text

    def checkIfElementExists(self, locator):
        assert self.findElement(locator), f"ERROR: Element '{locator}' not exists on this page."

    def checkIfElementNotExists(self, locator):
        assert len(self.findElements(locator)) == 0, f"ERROR: Element '{locator}' exists on this page."

    def pressKey(self, locator, key):
        element = self.findElement(locator)
        if key == "ENTER":
            element.send_keys(Keys.ENTER)
        elif key == "SPACE":
            element.send_keys(Keys.SPACE)
        elif key == "TAB":
            element.send_keys(Keys.TAB)
