from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_cart_empty(self):
        self.wait_for_element_appear(*self.CART_EMPTY_MSG)
        #expected_text = 'Your cart is empty'
        self.verify_text('Your cart is empty', *CartPage.CART_EMPTY_MSG)

    def verify_cart_item(self, product):
        self.wait_for_element_appear(*self.CART_ITEM_TITLE)
        self.verify_partial_text(product, *self.CART_ITEM_TITLE)
