import conftest


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
