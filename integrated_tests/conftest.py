import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def selenium_options():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    return chrome_options


@pytest.fixture()
def selenium_driver(selenium_options):

    drivers = []

    def _make_selenium_driver(use=False):
        if use is True:
            driver = webdriver.Chrome(
                executable_path='integrated_tests/webdrivers/chromedriver', options=selenium_options)
            drivers.append(driver)
            return driver
        else:
            driver = webdriver.Chrome(
                executable_path='integrated_tests/webdrivers/chromedriver', options=None)
            drivers.append(driver)
            return driver

    yield _make_selenium_driver

    for driver in drivers:
        driver.close()
