import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from config.config_reader import get_config


@pytest.fixture
def driver():

    config = get_config()

    chrome_options = Options()

    chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--no-sandbox")

    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_options.add_argument("--window-size=1920,1080")


    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.maximize_window()

    yield driver

    driver.quit()
