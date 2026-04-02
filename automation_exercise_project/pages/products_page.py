from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductsPage(BasePage):

    PRODUCTS_TITLE = "//h2[text()='All Products']"

    PRODUCT_CARDS = "//div[@class='product-image-wrapper']"

    PRODUCT_NAMES = "//div[@class='productinfo text-center']/p"

    SEARCH_INPUT = "//input[@id='search_product']"

    SEARCH_BTN = "//button[@id='submit_search']"

    # stable button inside productinfo section
    FIRST_PRODUCT_ADD_BTN = "(//div[@class='productinfo text-center']//a[contains(text(),'Add to cart')])[1]"



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



    # CI stable add to cart

    def add_first_product_to_cart(self):

        add_btn = self.wait.until(

            lambda d: d.find_element(By.XPATH, self.FIRST_PRODUCT_ADD_BTN)

        )



        self.driver.execute_script(

            "arguments[0].click();",

            add_btn

        )



    # CI stable navigation

    def view_cart(self):

        self.driver.get("https://automationexercise.com/view_cart")
