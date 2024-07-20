from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# Verify Cart empty message:
@then("Verify “Your cart is empty” message is shown")
def verify_cart_is_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_text == actual_text, f'Expected "{expected_text}" did not match "{actual_text}"'

@then('Verify 1 item text is shown')
def verify_item_text_is_shown(context):
    expected_text = '1 item'
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='1 item']").text
    assert expected_text in actual_text, f'Expected "{expected_text}" did not match "{actual_text}"'


