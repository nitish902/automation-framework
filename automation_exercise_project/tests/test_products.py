from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
import pytest
from utils.excel_reader import get_search_data


class TestProducts:


    def test_products_page(self, driver):

        home = HomePage(driver)

        home.open()

        home.go_to_products()

        products = ProductsPage(driver)

        assert products.is_products_page_loaded()


    def test_product_count(self, driver):

        home = HomePage(driver)

        home.open()

        home.go_to_products()

        products = ProductsPage(driver)

        count = products.get_product_count()

        print("Product count:", count)

        assert count > 0


    def test_get_product_names(self, driver):

        home = HomePage(driver)

        home.open()

        home.go_to_products()

        products = ProductsPage(driver)

        names = products.get_all_product_names()

        print(names)

        assert len(names) > 0


    def test_add_product_to_cart(self, driver):

        home = HomePage(driver)

        home.open()

        home.go_to_products()

        products = ProductsPage(driver)

        products.add_first_product_to_cart()

        products.view_cart()

        assert "view_cart" in driver.current_url


    def test_product_visible_in_cart(self, driver):

        home = HomePage(driver)

        home.open()

        home.go_to_products()

        products = ProductsPage(driver)

        products.add_first_product_to_cart()

        products.view_cart()

        cart = CartPage(driver)

        names = cart.get_cart_products()

        print(names)

        assert len(names) > 0


    def test_remove_product(self, driver):

        home = HomePage(driver)

        home.open()

        home.go_to_products()

        products = ProductsPage(driver)

        products.add_first_product_to_cart()

        products.view_cart()

        cart = CartPage(driver)

        cart.remove_product()

        assert cart.is_cart_empty()


    @pytest.mark.parametrize("search_item", get_search_data())
    def test_search_product_ddt(self, driver, search_item):

       home = HomePage(driver)

       home.open()

       home.go_to_products()

       products = ProductsPage(driver)

       products.search_product(search_item)

       names = products.get_all_product_names()

       print("Searching:", search_item)

       print("Results:", names)

       assert len(names) > 0