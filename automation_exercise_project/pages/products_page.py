from pages.base_page import BasePage


class ProductsPage(BasePage):

    PRODUCTS_TITLE = "//h2[text()='All Products']"

    PRODUCT_NAMES = "//div[@class='productinfo text-center']/p"

    PRODUCT_LINKS = "//div[@class='productinfo text-center']/p/../a"

    SEARCH_INPUT = "//input[@id='search_product']"

    SEARCH_BTN = "//button[@id='submit_search']"

    ADD_TO_CART_BTN_PRODUCT_PAGE = "//button[contains(text(),'Add to cart')]"



    def is_products_page_loaded(self):

        return self.find(self.PRODUCTS_TITLE).is_displayed()



    def get_product_count(self):

        return len(self.finds(self.PRODUCT_LINKS))



    def get_all_product_names(self):

        elements = self.finds(self.PRODUCT_NAMES)

        return [e.text for e in elements]



    def search_product(self, product_name):

        self.type(self.SEARCH_INPUT, product_name)

        self.click(self.SEARCH_BTN)



    # open first product page

    def open_first_product(self):

        products = self.finds(self.PRODUCT_LINKS)

        first_product = products[0]

        self.driver.execute_script(

            "arguments[0].click();",

            first_product

        )



    # add to cart from product page

    def add_first_product_to_cart(self):

        self.open_first_product()

        self.click(self.ADD_TO_CART_BTN_PRODUCT_PAGE)



    # open cart page directly

    def view_cart(self):

        self.driver.get("https://automationexercise.com/view_cart")from pages.base_page import BasePage


class ProductsPage(BasePage):

    PRODUCTS_TITLE = "//h2[text()='All Products']"

    PRODUCT_NAMES = "//div[@class='productinfo text-center']/p"

    PRODUCT_LINKS = "//div[@class='productinfo text-center']/p/../a"

    SEARCH_INPUT = "//input[@id='search_product']"

    SEARCH_BTN = "//button[@id='submit_search']"

    ADD_TO_CART_BTN_PRODUCT_PAGE = "//button[contains(text(),'Add to cart')]"



    def is_products_page_loaded(self):

        return self.find(self.PRODUCTS_TITLE).is_displayed()



    def get_product_count(self):

        return len(self.finds(self.PRODUCT_LINKS))



    def get_all_product_names(self):

        elements = self.finds(self.PRODUCT_NAMES)

        return [e.text for e in elements]



    def search_product(self, product_name):

        self.type(self.SEARCH_INPUT, product_name)

        self.click(self.SEARCH_BTN)



    # open first product page

    def open_first_product(self):

        products = self.finds(self.PRODUCT_LINKS)

        first_product = products[0]

        self.driver.execute_script(

            "arguments[0].click();",

            first_product

        )



    # add to cart from product page

    def add_first_product_to_cart(self):

        self.open_first_product()

        self.click(self.ADD_TO_CART_BTN_PRODUCT_PAGE)



    # open cart page directly

    def view_cart(self):

        self.driver.get("https://automationexercise.com/view_cart")
