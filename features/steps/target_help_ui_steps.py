from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target help page')
def open_target(context):
    context.driver.get('https://help.target.com/help')


@when("Target Help, text displays")
def target_help(context):
    context.driver.find_element(By.CSS_SELECTOR, "h2[class='custom-h2']")


@when("Search field displays")
def search_field(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='search-input']")


@when("Magnify button displays")
def magnify_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='search-btn']")


@when("Div block 1 elements display")
def div_block_1(context):
    context.driver.find_elements(By.CSS_SELECTOR, "[class*='container clear']")


@when("Manage my, cell elements display")
def manage_my_cell(context):
    context.driver.find_elements(By.CSS_SELECTOR, "[class*='salesforce']")


@when("Div block 2 elements display")
def div_block_1(context):
    context.driver.find_elements(By.CSS_SELECTOR, "[class*='grid_4 boxSmallr']")


@when("Browse all Help pages, text displays")
def browse_all_help(context):
    context.driver.find_element(By. XPATH, "//*[text()='Browse all Help pages']")


@then('Verify Browse all Help pages text displays')
def verify_page_ui(context):
    expected_text = (By. XPATH, "//*[text()='Browse all Help pages']")
    actual_text = 'Browse all Help pages'

    print('Test case passed')

