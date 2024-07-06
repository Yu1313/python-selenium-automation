from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# Click on Cart icon
@when("Click on Cart icon")
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


# Verify Cart empty message:
@then("Verify “Your cart is empty” message is shown")
def verify_cart_is_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    print(actual_text)




