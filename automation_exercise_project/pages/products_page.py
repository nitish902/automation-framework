from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ProductsPage(BasePage):

    PRODUCTS_TITLE = "//h2[text()='All Products']"

    PRODUCT_CARDS = "//div[@class='product-image-wrapper']"

    PRODUCT_NAMES = "//div[@class='productinfo text-center']/p"

    SEARCH_INPUT = "//input[@id='search_product']"

    SEARCH_BTN = "//button[@id='submit_search']"

    VIEW_CART_BTN = "//u[text()='View Cart']"



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



    def add_first_product_to_cart(self):

        products = self.finds(self.PRODUCT_CARDS)

        first_product = products[0]



        ActionChains(self.driver).move_to_element(first_product).perform()



        add_btn = first_product.find_element(
            By.XPATH,
            ".//a[contains(text(),'Add to cart')]"
        )



        self.driver.execute_script(
            "arguments[0].click();",
            add_btn
        )



    def view_cart(self):

        modal = self.wait.until(
            lambda d: d.find_element(By.XPATH, "//div[@class='modal-content']")
        )

        view_cart_btn = modal.find_element(
            By.XPATH,
            ".//u[text()='View Cart']"
        )

        self.driver.execute_script(
            "arguments[0].click();",
            view_cart_btn
        )
