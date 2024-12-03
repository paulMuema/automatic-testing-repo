import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def driver():
    # Initialize the WebDriver
    driver_instance = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver_instance
    # Quit the driver after the tests
    driver_instance.quit()

class TestLoadingTime:

    def test_page_load_time(self, driver):
        start_time = time.time()  # Record the start time
        driver.get("https://www.saucedemo.com/")  # Load the page
        end_time = time.time()  # Record the end time

        load_time = end_time - start_time  # Calculate the page load time
        assert load_time < 3, f"Page load time is too slow: {load_time:.2f} seconds"

    def test_element_load_time(self, driver):
        driver.get("https://www.saucedemo.com/")
        start_time = time.time()  # Start timing
        element = driver.find_element(By.ID, "user-name")  # Locate an element
        end_time = time.time()  # End timing

        load_time = end_time - start_time
        assert load_time < 2, f"Element load time is too slow: {load_time:.2f} seconds"
