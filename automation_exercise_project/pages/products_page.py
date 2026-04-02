from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class ProductsPage(BasePage):

    # locators

    PRODUCTS_TITLE = "//h2[text()='All Products']"

    PRODUCT_CARDS = "//div[@class='product-image-wrapper']"

    PRODUCT_NAMES = "//div[@class='productinfo text-center']/p"

    ADD_TO_CART_BTNS = "//a[contains(text(),'Add to cart')]"

    VIEW_CART_BTN = "//u[text()='View Cart']"

    SEARCH_INPUT = "//input[@id='search_product']"

    SEARCH_BTN = "//button[@id='submit_search']"



    # page loaded validation

    def is_products_page_loaded(self):

        return self.find(self.PRODUCTS_TITLE).is_displayed()



    # count products

    def get_product_count(self):

        return len(self.finds(self.PRODUCT_CARDS))



    # get all product names

    def get_all_product_names(self):

        elements = self.finds(self.PRODUCT_NAMES)

        return [e.text for e in elements]



    # search product

    def search_product(self, product_name):

        self.type(self.SEARCH_INPUT, product_name)

        self.click(self.SEARCH_BTN)



    # add first product to cart (CI stable)

    def add_first_product_to_cart(self):

        products = self.finds(self.PRODUCT_CARDS)

        first_product = products[0]



        # hover on product

        ActionChains(self.driver).move_to_element(first_product).perform()



        add_buttons = self.finds(self.ADD_TO_CART_BTNS)

        first_add_btn = add_buttons[0]



        # javascript click (more stable in CI)

        self.driver.execute_script(

            "arguments[0].click();",

            first_add_btn

        )



    # click view cart popup button

    def view_cart(self):

        self.wait_for(self.VIEW_CART_BTN)

        view_cart_btn = self.find(self.VIEW_CART_BTN)



        self.driver.execute_script(

            "arguments[0].click();",

            view_cart_btn

        )
