from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException


class ProductPage(BasePage):
    def get_strong_text_from_element(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            return self.get_text_from_element(*ProductPageLocators.STRONG, element)
        except NoSuchElementException:
            return ''

    def get_product_data(self):
        product_data = (
            self.get_text_from_element(*ProductPageLocators.PRODUCT_NAME),
            self.get_text_from_element(*ProductPageLocators.PRODUCT_PRICE)
        )
        return product_data

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    def should_not_have_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_PRODUCT_ADDED), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_PRODUCT_ADDED), \
            "Success message has not disappeared, but should have"

    def should_be_added_to_basket(self, product_name, product_price):
        self.should_be_same_name(product_name)
        self.should_be_same_price(product_price)

    def should_be_same_name(self, product_name):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_ADDED),\
            "Product name message is not presented"

        product_name_actual = self.get_strong_text_from_element(*ProductPageLocators.ALERT_PRODUCT_ADDED)
        assert product_name == product_name_actual, \
            f"Product name is not the same: expected {product_name}, got {product_name_actual}"

    def should_be_same_price(self, product_price):
        assert self.is_element_present(*ProductPageLocators.ALERT_BASKET_PRICE),\
            "Product price message is not presented"

        product_price_actual = self.get_strong_text_from_element(*ProductPageLocators.ALERT_BASKET_PRICE)
        assert product_price == product_price_actual, \
            f"Product price is not the same: expected {product_price}, got {product_price_actual}"
