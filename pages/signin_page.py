from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SigninPage(Page):
    ACTUAL_SIGNIN_TEXT = (By.XPATH, "//*[span='Sign into your Target account']")
    INPUT_EMAIL = (By.CSS_SELECTOR, "input#username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input#password")
    SIGNIN_WITH_PASSWORD_BTN = (By.CSS_SELECTOR, "button#login")

    def verify_sign_in_form(self):
        self.wait_for_element_appear(*self.ACTUAL_SIGNIN_TEXT)
        self.verify_text('Sign into your Target account', *self.ACTUAL_SIGNIN_TEXT)

    def input_email_and_password(self, email, password):
        self.input_text('katyaraalex@luanbeta.click', *self.INPUT_EMAIL, )
        self.input_text('*******', *self.INPUT_PASSWORD, )

    def click_signin_with_password(self):
        self.wait_and_click(*self.SIGNIN_WITH_PASSWORD_BTN)

    def verify_logged_in(self):
        self.wait_for_element_disappear(*self.ACTUAL_SIGNIN_TEXT)
