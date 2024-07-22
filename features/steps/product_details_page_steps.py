from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


# COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li")
# SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")
SIZE_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li")
SELECTED_SIZE = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


# @given('Open target product {product_id} page')
# def open_target(context, product_id):
#     context.driver.get(f'https://www.target.com/p/{product_id}')
#     sleep(8)
#
#
# @then('Verify user can click through colors')
# def click_and_verify_colors(context):
#     expected_colors = ['Beige', 'Black', 'Pink', 'Light Purple']
#     actual_colors = []
#
#     colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
#     for color in colors:
#         color.click()
#
#         selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
#         print('Current color', selected_color)
#
#         selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
#         actual_colors.append(selected_color)
#         print(actual_colors)
#
#     assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

@given("Open target product {men_shoes} page")
def open_target(context, men_shoes):
    context.driver.get(f'https://www.target.com/p/{men_shoes}')
    sleep(8)


@then('Verify user can click through sizes')
def click_and_verify_sizes(context):
    expected_sizes = ['8.5', '9', '9.5', '10', '10.5', '11']
    actual_sizes = []

    sizes = context.driver.find_elements(*SIZE_OPTIONS)  # [webelement1, webelement2, webelement3]
    for size in sizes[0:6]:
        size.click()

        selected_size = context.driver.find_element(*SELECTED_SIZE).text  # 'Color\nBlack'
        print('Current size', selected_size)

        selected_size = selected_size.split('\n')[1]  # remove 'Size\n' part, keep Black'
        actual_sizes.append(selected_size)
        print(actual_sizes)

    assert expected_sizes == actual_sizes, f'Expected {expected_sizes} did not match actual {actual_sizes}'

