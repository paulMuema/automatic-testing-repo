import pytest
from selenium import webdriver
from utilities.test_data import TestData

@pytest.fixture(params=['firefox', 'chrome', 'edge'])
def initialize_driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'edge':
        driver = webdriver.Edge()

    request.cls.driver = driver
    print("Browser:",request.param)
    driver.get(TestData.url)
    yield
    print("Close Driver")
    driver.close()

