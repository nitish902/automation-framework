import pytest
from selenium import webdriver
from config.config_reader import get_config
import os
from datetime import datetime


@pytest.fixture
def driver():

    config = get_config()

    browser = config["browser"]

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "edge":
        driver = webdriver.Edge()

    else:
        driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    driver.quit()


# screenshot hook
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            file_name = f"screenshots/{item.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"

            driver.save_screenshot(file_name)

            print(f"\nScreenshot saved: {file_name}")