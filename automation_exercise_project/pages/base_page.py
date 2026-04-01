from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def find(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)


    def finds(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)


    def click(self, xpath):
        self.find(xpath).click()


    def type(self, xpath, text):
        element = self.find(xpath)
        element.clear()
        element.send_keys(text)


    def get_text(self, xpath):
        return self.find(xpath).text


    def wait_for(self, xpath, time=10):
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )