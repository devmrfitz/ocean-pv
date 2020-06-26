import pytest
from selenium.webdriver.common.keys import Keys


@pytest.mark.browser
def test_random(selenium_driver):
    driver = selenium_driver
    driver.get('https://duckduckgo.com/')
    element = driver.find_element_by_id('search_form_input_homepage')
    element.send_keys('IgnisDa', Keys.RETURN)
    assert 'IgnisDa' in driver.current_url


if __name__ == '__main__':
    pytest.main()
