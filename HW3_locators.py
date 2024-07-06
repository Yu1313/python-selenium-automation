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

# PART 1. Find the most optimal locators for Create Account on amazon.com
# (Registration) page elements:
# 1. Amazon logo
driver.find_element(By.CSS_SELECTOR, "i[aria-label='Amazon']")
# 2. Create account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
# 3. Your name field
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
# 4. Email field
driver.find_element(By.CSS_SELECTOR, "input#ap_email")
# 5. password field
driver.find_element(By.CSS_SELECTOR, "input#ap_password")
# 6. "Passwords must be at least 6 characters."
driver.find_element(By.CSS_SELECTOR, "//div[contains(text(), 'Passwords must be')]")
# 7. Re-enter password field
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")
# 8. Create your amazon account button
driver.find_element(By.CSS_SELECTOR, "[class='a-button-input'][type='submit']")
# 9. Condition of Use link
driver.find_element(By.CSS_SELECTOR, "div.a-box div#legalTextRow [href*='condition']")
# 10. Privacy Notice link
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_privacy_notice']")
# 11. Sign in link
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href*='/ap/signin']")

