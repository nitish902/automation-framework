from pages.base_page import BasePage


class ProductsPage(BasePage):

    PRODUCTS_TITLE = "//h2[text()='All Products']"

    PRODUCT_CARDS = "//div[@class='product-image-wrapper']"

    PRODUCT_NAMES = "//div[@class='productinfo text-center']/p"

    ADD_TO_CART_FIRST = "(//a[contains(text(),'Add to cart')])[1]"

    VIEW_CART_BTN = "//u[text()='View Cart']"

    SEARCH_INPUT = "//input[@id='search_product']"

    SEARCH_BTN = "//button[@id='submit_search']"


    def is_products_page_loaded(self):
        self.wait_for(self.PRODUCTS_TITLE)
        return self.find(self.PRODUCTS_TITLE).is_displayed()


    def get_product_count(self):
        self.wait_for(self.PRODUCT_CARDS)
        return len(self.finds(self.PRODUCT_CARDS))


    def get_all_product_names(self):
        elements = self.finds(self.PRODUCT_NAMES)
        return [e.text for e in elements]


    def add_first_product_to_cart(self):
        self.wait_for(self.ADD_TO_CART_FIRST)
        self.click(self.ADD_TO_CART_FIRST)


    def view_cart(self):
        self.wait_for(self.VIEW_CART_BTN)
        self.click(self.VIEW_CART_BTN)


    def search_product(self, product_name):
        self.wait_for(self.SEARCH_INPUT)
        self.type(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BTN)