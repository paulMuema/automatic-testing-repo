from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
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

@pytest.mark.usefixtures("initialize_driver")
class BaseTest:
  pass
class TestDrivers(BaseTest):
    def test_multiple_browser(self):
        self.driver.get(TestData.url)
        header = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]').text
        print("Hedear :", header)
        assert header == 'Swag Labs'