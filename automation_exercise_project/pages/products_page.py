from pages.base_page import BasePage


class ProductsPage(BasePage):

    PRODUCTS_TITLE = "//h2[text()='All Products']"

    PRODUCT_CARDS = "//div[@class='product-image-wrapper']"

    PRODUCT_NAMES = "//div[@class='productinfo text-center']/p"

    SEARCH_INPUT = "//input[@id='search_product']"

    SEARCH_BTN = "//button[@id='submit_search']"

    ADD_TO_CART_BTNS = "//a[contains(text(),'Add to cart')]"



    def is_products_page_loaded(self):

        return self.find(self.PRODUCTS_TITLE).is_displayed()



    def get_product_count(self):

        return len(self.finds(self.PRODUCT_CARDS))



    def get_all_product_names(self):

        elements = self.finds(self.PRODUCT_NAMES)

        return [e.text for e in elements]



    def search_product(self, product_name):

        self.type(self.SEARCH_INPUT, product_name)

        self.click(self.SEARCH_BTN)



    # stable add to cart

    def add_first_product_to_cart(self):

        buttons = self.finds(self.ADD_TO_CART_BTNS)

        first_btn = buttons[0]



        self.driver.execute_script(

            "arguments[0].click();",

            first_btn

        )



    # go to cart directly (CI stable)

    def view_cart(self):

        self.driver.get("https://automationexercise.com/view_cart")
