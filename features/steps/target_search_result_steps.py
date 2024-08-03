from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC  #alias to make this short in code

# THIS IS CALLED UNPACKING
ADD_ITEM_TO_CART_BTN = (By. CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="content-wrapper"] h4')
SIDE_NAV_ADD_TO_CART = (By. CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
VIEW_CART_AND_CHECKOUT = (By.CSS_SELECTOR, "[href='/cart']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')


@when('Add item to cart')
def add_item_to_cart(context):
    context.app.search_results_page.search_add_item_to_cart()
    # context.driver.wait.until(EC.element_to_be_clickable(ADD_ITEM_TO_CART_BTN)).click()
    # sleep(3)
    # context.driver.wait.until(*ADD_ITEM_TO_CART_BTN).click()
# context.driver.find_element(By. CSS_SELECTOR "[id*='addToCartButton']")[0].click--  clicks on 1st add to cart button


@when('Store product name')
def store_product_name(context):
    context.app.search_results_page.store_product_name()
    # context.product_info = context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME)).text
    # context.product_info = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    # print(f'Product stored: {context.product_info}')


@when('Add to cart from side nav')
def add_to_cart(context):
    context.app.search_results_page.side_nav_add_to_cart()
    # context.driver.wait.until(EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART)).click()
    # context.driver.find_element(*SIDE_NAV_ADD_TO_CART).click()
    # sleep(5)


@when('View cart & checkout')
def exit_cart(context):
    context.app.search_results_page.view_cart_and_checkout()
    # context.driver.wait.until(EC.element_to_be_clickable(VIEW_CART_AND_CHECKOUT)).click()
    # sleep(5)
    # context.driver.find_element(*VIEW_CART_AND_CHECKOUT).click()


@when('Hover favorites icon')
def hover_fav_icon(context):
    context.app.search_results_page.hover_fav_icon()


@then('Favorites tooltip is shown')
def verify_fav_tooltip(context):
    context.app.search_results_page.verify_fav_tooltip()


@then('Verify search worked for {expected_product}')
def verify_search_worked(context, expected_product):
    context.app.search_results_page.verify_search_results(expected_product)
    # actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    # # asserts compares values assert 1==1 true
    # assert product in actual_text, f'Expected text {product} is not in actual text {actual_text}'


@then('Verify correct search results URL opens for {expected_product}')
def verify_search_worked(context, expected_product):
    context.app.search_results_page.verify_product_in_url(expected_product)
    # url = context.driver.current_url
    # assert product in url, f'{product} not in {url}'

    print('Test case passed')


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in all_products[0:4]:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)