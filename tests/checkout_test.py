import pytest
from pages.base_page import BasePage
from utilities.test_data import TestData
from selenium import webdriver

class TestCheckout(BasePage):

    def __init__(self):
        super().__init__(self)

    def checkout(self, username_input, password_input):
        self.open(TestData.url)
        self.set(TestData.username_input_field, username_input)
        self.set(TestData.password_input_field, password_input)
        self.click(TestData.submit_btn_field)
        self.click(TestData.product1_add_to_cart_field)
        self.click(TestData.shopping_cart_link)
        self.click(TestData.checkout_btn)
        self.set(TestData.first_name_field, TestData.first_name_keys)
        self.set(TestData.last_name_field, TestData.last_name_keys)
        self.set(TestData.zip_code_field, TestData.zip_code_key)
        self.click(TestData.continue_btn)
        self.click(TestData.finish_btn)
        confirmation_message = self.get_text(TestData.confirmation_message)
        assert confirmation_message == "Thank you for your order!"
        self.close()

def test_complete_checkout():
    test_checkout = TestCheckout()
    test_checkout.checkout(TestData.username, TestData.password)
