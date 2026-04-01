from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


class TestE2E:


    def test_complete_user_flow(self, driver):

        # open homepage
        home = HomePage(driver)

        home.open()

        assert home.is_home_page_loaded()


        # go to products page
        home.go_to_products()

        products = ProductsPage(driver)

        assert products.is_products_page_loaded()


        # search product
        products.search_product("Tshirt")

        product_names = products.get_all_product_names()

        print("Search results:", product_names)

        assert len(product_names) > 0


        # add product to cart
        products.add_first_product_to_cart()

        products.view_cart()

        assert "view_cart" in driver.current_url


        # verify cart items
        cart = CartPage(driver)

        cart_products = cart.get_cart_products()

        print("Cart products:", cart_products)

        assert len(cart_products) > 0


        # remove product
        cart.remove_product()


        # verify cart empty
        assert cart.is_cart_empty()
        