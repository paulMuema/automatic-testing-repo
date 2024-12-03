from typing import Tuple

from selenium.webdriver.common.by import By


class TestData:
    url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    username_input_field = (By.ID, "user-name")
    password_input_field = (By.ID, "password")
    submit_btn_field = (By.ID, "login-button")
    url_products_page = 'https://www.saucedemo.com/inventory.html'
    product1_add_to_cart_field = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    product2_add_to_cart_field = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    shopping_cart_link = (By.CLASS_NAME, 'shopping_cart_link')
    checkout_btn = (By.ID, 'checkout')
    first_name_field = (By.ID, 'first-name')
    last_name_field = (By.ID, 'last-name')
    zip_code_field = (By.ID, 'postal-code')
    first_name_keys = 'Dele'
    last_name_keys = 'Ali'
    zip_code_key = '120036'
    continue_btn = (By.ID, 'continue')
    finish_btn = (By.ID, 'finish')
    confirmation_message = (By.XPATH, '/html/body/div/div/div/div[2]/h2')


