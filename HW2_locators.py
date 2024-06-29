from selenium import webdriver  # allows pycharm to work with selenium elements
from selenium.webdriver.common.by import By  # allows pycharm to work with selenium locators
from selenium.webdriver.chrome.service import Service      # allows selenium to connect with chrome
from webdriver_manager.chrome import ChromeDriverManager  # allows selenium to connect with chrome
from time import sleep  # allows to stop execution of code

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()    # connects to  chrome

# create a new Chrome browser instance
service = Service(driver_path)  # starts chrome
driver = webdriver.Chrome(service=service)  # starts chrome
driver.maximize_window()  # maximizes Chrome browser screen


# HW Part 1: Create locators + search strategy for these page elements of Amazon Sign in page:
# - Amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
# - Email field
driver.find_element(By.ID, 'ap_email')
# - Continue button
driver.find_element(By.ID, 'continue')
# - Conditions of use link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Conditions of Use']")
# - Privacy Notice link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(text(), 'Privacy')]")
# - Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
# - Forgot your password link
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")
# - Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')
# - Create your Amazon account
# button
driver.find_element(By.ID, 'createAccountSubmit')
