from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 15)



    def find(self, xpath):

        return self.wait.until(

            EC.presence_of_element_located((By.XPATH, xpath))

        )



    def finds(self, xpath):

        return self.wait.until(

            EC.presence_of_all_elements_located((By.XPATH, xpath))

        )



    def click(self, xpath):

        element = self.wait.until(

            EC.element_to_be_clickable((By.XPATH, xpath))

        )

        element.click()



    def type(self, xpath, text):

        element = self.wait.until(

            EC.visibility_of_element_located((By.XPATH, xpath))

        )

        element.clear()

        element.send_keys(text)



    def get_text(self, xpath):

        element = self.wait.until(

            EC.visibility_of_element_located((By.XPATH, xpath))

        )

        return element.text



    def wait_for(self, xpath):

        self.wait.until(

            EC.visibility_of_element_located((By.XPATH, xpath))

        )
