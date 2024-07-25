from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGNIN_HEADER = (By.XPATH, "//a[@data-test='@web/AccountLink']")
    SIGNIN_NAV = (By.XPATH, "//a[@data-test='accountNav-signIn']")

    def search_product(self, product):
        print('POM Layer:', product)
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        # wait for the page with search results to load
        sleep(6)

    def click_cart(self):
        self.wait_and_click(*self.CART_BTN)

    def click_signin_header(self):
        self.wait_and_click(*self.SIGNIN_HEADER)

    def click_signin_nav(self):
        self.wait_and_click(*self.SIGNIN_NAV)
