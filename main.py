from pages.login_page import Login
from pages.products_page import ProductsPage
from utilities.test_data import TestData

login = Login()
login.login_into_aplication(TestData.username,TestData.password)
cart = ProductsPage()
cart.add_to_cart(TestData.product1_add_to_cart_field)
