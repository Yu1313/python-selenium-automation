from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC  #alias to make this short in code


CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
CART_EMPTY_MSG = By.CSS_SELECTOR, "[data-test='boxEmptyMsg']"


# Verify Cart empty message:
@then("Verify “Your cart is empty” message is shown")
def verify_cart_is_empty(context):
    context.app.cart_page.verify_cart_empty()
    # expected_text = 'Your cart is empty'
    # actual_text = context.driver.wait_until(EC.visibility_of_element_located(CART_EMPTY_MSG)).text
    # assert expected_text == actual_text, f'Expected "{expected_text}" did not match "{actual_text}"'


@then('Verify cart has correct {product}')
def verify_product_name(context, product):
    context.app.cart_page.verify_cart_item(product)
    # actual_name = context.driver.wait.until(EC.visibility_of_element_located(CART_ITEM_TITLE)).text
    # print(f'Actual product in cart name: {actual_name}')
    # print(f'expected_product: {context.product_info}')
    # assert context.product_info in actual_name, f"Expected {context.product_info} but got {actual_name}"


@then('Verify cart has {amount} item(s)')
def verify_item_text_is_shown(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"





