import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.checkout
@pytest.mark.smoke
class TestCT04:
    def test_ct04_checkoutOneProduct(self):
        driver = conftest.driver
        #Login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()

        #Add Backpack to cart
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

        #Check cart
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        #Checkout
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("Lucas")
        driver.find_element(By.ID, "last-name").send_keys("Rosa")
        driver.find_element(By.ID, "postal-code").send_keys("88780-000")
        driver.find_element(By.ID, "continue").click()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        driver.find_element(By.ID, "finish").click()
        assert driver.find_element(By.XPATH, "//*[@class='complete-header']").is_displayed()
