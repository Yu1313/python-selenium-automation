from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# 4. Verify SignIn page opened:
@then("Verify Sign In form opened")
def verify_sign_in(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.XPATH, "//*[span='Sign into your Target account']").text
    print(actual_text)
