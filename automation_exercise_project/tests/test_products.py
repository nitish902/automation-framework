from pages.home_page import HomePage
from pages.products_page import ProductsPage


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

        assert count > 0



    def test_get_product_names(self, driver):

        home = HomePage(driver)

        home.open()

        home.go_to_products()

        products = ProductsPage(driver)

        names = products.get_all_product_names()

        assert len(names) > 0



    # stable cart navigation validation
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

        assert "view_cart" in driver.current_url



    def test_remove_product(self, driver):

        home = HomePage(driver)

        home.open()

        driver.get("https://automationexercise.com/view_cart")

        assert "view_cart" in driver.current_url



    # Data driven search test
    import pytest
    from utils.excel_reader import get_search_data


    @pytest.mark.parametrize("search_item", get_search_data())
    def test_search_product_ddt(self, driver, search_item):

        home = HomePage(driver)

        home.open()

        home.go_to_products()

        products = ProductsPage(driver)

        products.search_product(search_item)

        names = products.get_all_product_names()

        assert len(names) > 0
