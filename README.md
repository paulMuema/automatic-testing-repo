# AutoTestWeb
Automated testing framework for a Web Application done as a group of 4.

# Description
It uses Selenium Web Driver to carry our E2E testing of an ecommerce website called SurfLabs. Various functionalities are tested such as logging in, adding items to cart et cetera. It validates that certain elements are present and performs actions based on specific conditions.

# Objectives
- End-to-end flow for a customer buying a product
- Login functionality, add-to-cart functionality, registration functionality, and log out functionality
- Site functionality on multiple browsers

# Test Cases
- Opening the Web Page and maximizing the window
- Logging In
- Verifying Header
- Keying In Information
- Adding items to a cart
- Clicking buttons
- Logging Out

# Test Reporting

Used Allure. Commands used to generate report:
1. pytest --alluredir=allure-results
2. allure serve allure-results


# Technologies Used
- Python Language
- IDE (Visual Studio Code or PyCharm)
- Selenium and Pytest
- Allure
- Test Browsers Chrome, Edge, Firefox
