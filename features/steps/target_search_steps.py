from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://target.com')


@when('Search for product')
def search_product(context):
    # find search field and enter text
    context.driver.find_element(By.XPATH, "//input[@data-test='@web/Search/SearchInput']").send_keys('coffee')
    # Click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # after clicks search will wait until page load to verify results --will not get critical errors
    sleep(6)


@then('Verify search worked')
def verify_search_worked(context):
    expected_text = 'coffee'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    print(actual_text)
    # asserts compares values assert 1==1 true
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'

    print('Test case passed')