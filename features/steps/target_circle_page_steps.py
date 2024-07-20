from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify circle page has {number} benefits cell')
def verify_benefit_cells_count(context, number):
    number = int(number)
    cells = context.driver.find_elements(By.CSS_SELECTOR, "[class*='cell-item-content']")
    assert len(cells) == number, f'Expected {number} cells but got {len(cells)}'
    print('Test case Passed!')
