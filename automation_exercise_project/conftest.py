import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.config_reader import get_config


@pytest.fixture
def driver():

    config = get_config()

    browser = config["browser"]

    if browser == "chrome":

        service = Service(ChromeDriverManager().install())

        driver = webdriver.Chrome(service=service)

    else:

        service = Service(ChromeDriverManager().install())

        driver = webdriver.Chrome(service=service)


    driver.maximize_window()

    yield driver

    driver.quit()
