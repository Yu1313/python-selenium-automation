from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# Click SignIn button
@when("Click Sign In")
def sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
    sleep(5)


# 3. Click SignIn from side navigation
@when("From right side navigation menu, click Sign In")
def right_nav_signin(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(5)


# 4. Verify SignIn page opened:
@then("Verify Sign In form opened")
def verify_sign_in(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.XPATH, "//*[span='Sign into your Target account']").text
    print(actual_text)
