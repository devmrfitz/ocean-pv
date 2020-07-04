import pytest
from selenium.webdriver.common.keys import Keys
from time import sleep


@pytest.mark.browser
def test_random(selenium_driver, live_server):
    driver = selenium_driver(use=True)
    driver.get(live_server.url)
    assert 'IgnisDa' in driver.current_url


if __name__ == '__main__':
    pytest.main()
