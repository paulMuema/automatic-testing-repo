from selenium import webdriver

class BasePage:

    def __init__(self, driver):
        self.driver = webdriver.Firefox()

    def open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(*locator).click()

    def set(self,locator,value):
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text

    def close(self):
        self.driver.close()








