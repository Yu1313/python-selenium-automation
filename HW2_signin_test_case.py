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


# Part 2: Create a test case for the SignIn page using python & selenium script.
# Open https://www.target.com/
driver.get('https://www.target.com/')
# Click SignIn button
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
sleep(2)
# 3. Click SignIn from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(2)
# 4. Verify SignIn page opened:
expected_text = 'Sign into your Target account'
actual_text = driver.find_element(By.XPATH, "//*[span='Sign into your Target account']").text
print(actual_text)
