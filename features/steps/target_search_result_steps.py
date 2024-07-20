from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Add milk to cart')
def add_milk_to_cart(context):
    sleep(3)
    context.driver.find_element(By. CSS_SELECTOR, 'button[data-test="chooseOptionsButton"]').click()


@when('Add to cart')
def add_to_cart(context):
    context.driver.find_element(By. CSS_SELECTOR, "[data-test='orderPickupButton']").click()
    sleep(3)


@when('View cart & checkout')
def exit_cart(context):
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "[href='/cart']").click()


@then('Verify search worked for {product}')
def verify_search_worked(context, product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    # asserts compares values assert 1==1 true
    assert product in actual_text, f'Expected text {product} is not in actual text {actual_text}'


@then('Verify correct search results URL opens for {product}')
def verify_search_worked(context, product):
    url = context.driver.current_url
    assert product in url, f'{product} not in {url}'

    print('Test case passed')
