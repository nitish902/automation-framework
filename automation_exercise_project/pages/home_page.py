from pages.base_page import BasePage
from config.config_reader import get_config


class HomePage(BasePage):

    config = get_config()

    URL = config["url"]

    HOME_LOGO = "//img[@alt='Website for automation practice']"

    PRODUCTS_BTN = "//a[@href='/products']"


    def open(self):

        self.driver.get(self.URL)


    def is_home_page_loaded(self):

        self.wait_for(self.HOME_LOGO)

        return self.find(self.HOME_LOGO).is_displayed()


    def go_to_products(self):

        self.click(self.PRODUCTS_BTN)