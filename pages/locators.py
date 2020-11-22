from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_PRODUCT_ADDED = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")
    ALERT_BASKET_PRICE = (By.CSS_SELECTOR, "#messages .alert-info")
    STRONG = (By.CSS_SELECTOR, "strong")
