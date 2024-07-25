from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_ITEM_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="content-wrapper"] h4')
    SIDE_NAV_ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    VIEW_CART_AND_CHECKOUT = (By.CSS_SELECTOR, "[href='/cart']")

    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TXT)

    def verify_product_in_url(self, expected_product):
        self.verify_partial_url(expected_product)

    def search_add_item_to_cart(self):
        self.wait_and_click(*self.ADD_ITEM_TO_CART_BTN)

    def store_product_name(self):
        self.wait_for_element_appear(*self.SIDE_NAV_PRODUCT_NAME)
        product_name = self.find_element(*self.SIDE_NAV_PRODUCT_NAME).text
        print("The product name is: ", product_name)

    def side_nav_add_to_cart(self):
        self.wait_and_click(*self.SIDE_NAV_ADD_TO_CART)

    def view_cart_and_checkout(self):
        self.wait_and_click(*self.VIEW_CART_AND_CHECKOUT)


