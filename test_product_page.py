from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest


product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{n}" for n in range(10)]

# ?promo=offer7 has expected bug on the page
urls[7] = pytest.param(urls[7], marks=pytest.mark.xfail)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


class TestAddToBasket():
    @pytest.mark.parametrize('link', urls)
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

    def test_guest_cant_see_success_message(browser):
        product_page = ProductPage(browser, product_base_link)
        product_page.open()
        product_page.should_not_have_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(browser):
        product_page = ProductPage(browser, product_base_link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.should_disappear_success_message()
