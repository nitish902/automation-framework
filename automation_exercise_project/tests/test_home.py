from pages.home_page import HomePage


class TestHome:


    def test_home_page_loads(self, driver):

        home = HomePage(driver)

        home.open()

        assert home.is_home_page_loaded()