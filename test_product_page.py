from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
import pytest
import time


product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
promo_urls = [f"{product_base_link}/?promo=offer{n}" for n in range(10)]
# ?promo=offer7 has expected bug on the page
promo_urls[7] = pytest.param(promo_urls[7], marks=pytest.mark.xfail)


@pytest.mark.login_guest
class TestLoginFromProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, product_base_link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
    basket_page.should_have_empty_text()


@pytest.mark.need_review
@pytest.mark.parametrize('link', promo_urls)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_data = product_page.get_product_data()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_added_to_basket(*product_data)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, product_base_link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_have_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, product_base_link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_disappear_success_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_url = "http://selenium1py.pythonanywhere.com/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + '_pswd'

        login_page = LoginPage(browser, login_url)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, product_base_link)
        product_page.open()
        product_data = product_page.get_product_data()
        product_page.add_product_to_basket()
        product_page.should_be_added_to_basket(*product_data)

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, product_base_link)
        product_page.open()
        product_page.should_not_have_success_message()

