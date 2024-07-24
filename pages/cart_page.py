from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = By.CSS_SELECTOR, "[data-test='boxEmptyMsg']"

    def verify_cart_empty(self):
        expected_text = 'Your cart is empty'
        #actual_text = self.driver.find_element(*self.CART_EMPTY_MSG).text
        actual_text = self.find_element(*self.CART_EMPTY_MSG).text
        #self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)
        assert actual_text in expected_text, f'Expected {expected_text} but got {actual_text}'
