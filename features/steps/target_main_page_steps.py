from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://target.com')


@when('Search for {product}')
def search_product(context, product):
    # find search field and enter text
    context.driver.find_element(By.XPATH, "//input[@data-test='@web/Search/SearchInput']").send_keys(product)
    # Click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # after clicks search will wait until page load to verify results --will not get critical errors
    sleep(2)


# Click SignIn button
@when("Click Sign In")
def sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
    sleep(5)


# 3. Click SignIn from side navigation
@when("From right side navigation menu, click Sign In")
def right_nav_signin(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(5)


# Click on Cart icon
@when("Click on Cart icon")
def click_cart(context):
    sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@then('Verify header is shown')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='utilityHeaderContainer__k6A7s']")


@then('Verify header has {number} links')
def verify_header_6_links(context, number):
    number = int(number) # '6' => 6
    links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")
    assert len(links) == number, f'Expected {number} links but got {len(links)}'


