from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.send_keys(*LoginPageLocators.REGISTRATION_EMAIL_INPUT, email)
        self.send_keys(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT, password)
        self.send_keys(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM_INPUT, password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    def send_keys(self, how, what, text):
        element = self.browser.find_element(how, what)
        element.send_keys(text)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' is not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
