from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC  #alias to make this short in code

# THIS IS CALLED UNPACKING
ADD_ITEM_TO_CART_BTN = (By. CSS_SELECTOR, "[id*='addToCartButton']")
#SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="content-wrapper"] h4')
SIDE_NAV_ADD_TO_CART = (By. CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
VIEW_CART_AND_CHECKOUT = (By.CSS_SELECTOR, "[href='/cart']")


@when('Add milk to cart')
def add_milk_to_cart(context):
    sleep(3)
    context.driver.find_element(*ADD_ITEM_TO_CART_BTN).click()
    #context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME))
# context.driver.find_element(By. CSS_SELECTOR "[id*='addToCartButton']")[0].click--  clicks on 1st add to cart button


@when('Store product name')
def store_product_name(context):
    context.product_info = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(f'Product stored: {context.product_info}')


@when('Add to cart from side nav')
def add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART).click()
    sleep(5)
    #context.driver.wait.until(EC.visibility_of_element_located(VIEW_CART_AND_CHECKOUT))


@when('View cart & checkout')
def exit_cart(context):
    sleep(5)
    context.driver.find_element(*VIEW_CART_AND_CHECKOUT).click()


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
