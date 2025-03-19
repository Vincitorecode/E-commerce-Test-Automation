E-commerce Test Automation
This repository contains automated test scripts for a fictional eCommerce website using Selenium WebDriver and Python. The tests cover key functionalities such as login, search, cart, and checkout processes to ensure the smooth operation of an online store.

Test Overview
1. Login Test - test_login.py
Description: Verifies the login functionality for the eCommerce site (using Sauce Demo as an example).
Steps:
Navigate to the login page.
Enter valid credentials (username: standard_user, password: secret_sauce).
Check if the user is successfully redirected to the homepage after logging in.
Outcome: The test will pass if the login is successful and the homepage is displayed.
2. Search Test - test_search.py
Description: Tests the search functionality to ensure that products can be searched and results are displayed correctly.
Steps:
Navigate to the search bar.
Enter a product name (e.g., "Sauce Labs Backpack").
Verify that the correct product appears in the search results.
Outcome: The test will pass if the correct product is displayed in the search results.
3. Cart Test - test_cart.py
Description: Automates the process of adding products to the shopping cart and verifies the cart functionality.
Steps:
Log in to the website.
Add a product to the cart.
Verify that the cart badge updates and displays the correct number of items.
Check if the added product is correctly shown in the cart.
Outcome: The test will pass if the product is added to the cart and displayed correctly.
4. Checkout Test - test_checkout.py
Description: Simulates the checkout process, ensuring that the steps from cart review to order completion work as expected.
Steps:
Add products to the cart.
Proceed to the checkout page.
Complete the payment process.
Verify that the order confirmation page appears after successful checkout.
Outcome: The test will pass if the order is successfully completed and confirmed.