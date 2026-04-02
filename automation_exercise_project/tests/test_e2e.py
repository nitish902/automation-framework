from pages.home_page import HomePage
from pages.products_page import ProductsPage


class TestE2E:


    def test_complete_user_flow(self, driver):

        home = HomePage(driver)

        home.open()

        assert home.is_home_page_loaded()



        home.go_to_products()

        products = ProductsPage(driver)

        assert products.is_products_page_loaded()



        products.search_product("Tshirt")

        names = products.get_all_product_names()

        assert len(names) > 0



        products.add_first_product_to_cart()

        products.view_cart()

        assert "view_cart" in driver.current_url     
