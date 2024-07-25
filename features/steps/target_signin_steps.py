from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC  #alias to make this short in code

ACTUAL_SIGNIN_TEXT = (By.XPATH, "//*[span='Sign into your Target account']")
INPUT_EMAIL = (By. CSS_SELECTOR, "input#username")
INPUT_PASSWORD = (By.CSS_SELECTOR, "input#password")
SIGNIN_WITH_PASSWORD_BTN = (By. CSS_SELECTOR, "button#login")


@when("input email and password on SignIn page")
def input_email_and_password(context):
    context.app.signin_page.input_email_and_password(INPUT_EMAIL, INPUT_PASSWORD)
    # context.driver.wait.until(EC.visibility_of_element_located(INPUT_EMAIL)).send_keys("katyaraalex@luanbeta.click")
    # context.driver.wait.until(EC.visibility_of_element_located(INPUT_PASSWORD)).send_keys("******")


@when("Click Sign in with password")
def click_sign_in_with_password(context):
    context.app.signin_page.click_signin_with_password()
    # context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_WITH_PASSWORD_BTN)).click()


@then("Verify user is logged in")
def verify_user_is_logged_in(context):
    context.app.signin_page.verify_logged_in()
    # context.driver.wait.until(EC.invisibility_of_element_located(ACTUAL_SIGNIN_TEXT))


# 4. Verify SignIn page opened:
@then("Verify Sign In form opened")
def verify_sign_in(context):
    context.app.signin_page.verify_sign_in_form()
    # expected_text = 'Sign into your Target account'
    # actual_text = context.driver.wait.until(EC.visibility_of_element_located(ACTUAL_SIGNIN_TEXT)).text
    # print(actual_text)
