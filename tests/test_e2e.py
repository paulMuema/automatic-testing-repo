import pytest
from pages.base_page import BasePage
from utilities.test_data import TestData
from selenium import webdriver

class TestE2E(BasePage):

    def __init__(self):
        super().__init__(self)

    def e2e(self,username_input,password_input,add_locator):
        self.open(TestData.url)
        self.set(TestData.username_input_field,username_input)
        self.set(TestData.password_input_field,password_input)
        self.click(TestData.submit_btn_field)
        self.click(add_locator)
        self.click(TestData.shopping_cart_link)
        self.click(TestData.checkout_btn)
        self.set(TestData.first_name_field,TestData.first_name_keys)
        self.set(TestData.last_name_field,TestData.last_name_keys)
        self.set(TestData.zip_code_field,TestData.zip_code_key)
        self.click(TestData.continue_btn)
        self.click(TestData.finish_btn)
        confirmation = self.get_text(TestData.confirmation_message)
        assert confirmation == 'Thank you for your order!'
        self.close()


def test1():
    test_e2e_object = TestE2E()
    test_e2e_object.e2e(TestData.username,TestData.password,TestData.product1_add_to_cart_field)


