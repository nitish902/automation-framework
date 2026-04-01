from pages.base_page import BasePage


class CartPage(BasePage):

    CART_PRODUCTS = "//td[@class='cart_description']/h4/a"

    REMOVE_BTN = "//a[@class='cart_quantity_delete']"

    EMPTY_CART_TEXT = "//b[text()='Cart is empty!']"


    def get_cart_products(self):
        elements = self.finds(self.CART_PRODUCTS)
        return [e.text for e in elements]


    def remove_product(self):
        self.wait_for(self.REMOVE_BTN)
        self.click(self.REMOVE_BTN)


    def is_cart_empty(self):
        self.wait_for(self.EMPTY_CART_TEXT)
        return self.find(self.EMPTY_CART_TEXT).is_displayed()