from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


# Verify Cart empty message:
@then("Verify “Your cart is empty” message is shown")
def verify_cart_is_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_text == actual_text, f'Expected "{expected_text}" did not match "{actual_text}"'


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    print(f'Actual product in cart name: {actual_name}')
    print(f'expected_product: {context.product_info}')
    assert context.product_info in actual_name, f"Expected {context.product_info} but got {actual_name}"


@then('Verify cart has {amount} item(s)')
def verify_item_text_is_shown(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"





