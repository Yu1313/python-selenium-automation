from selenium import webdriver  # allows pycharm to work with selenium elements
from selenium.webdriver.common.by import By  # allows pycharm to work with selenium locators
from selenium.webdriver.chrome.service import Service      # allows selenium to connect with chrome
from webdriver_manager.chrome import ChromeDriverManager  # allows selenium to connect with chrome
from time import sleep  # allows to stop execution of code

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()    # connects to chrome

# create a new Chrome browser instance
service = Service(driver_path)  # starts chrome
driver = webdriver.Chrome(service=service)  # starts chrome
driver.maximize_window()  # maximizes Chrome browser screen

# open the url
driver.get('https://www.target.com/')
# find search field and enter text
driver.find_element(By.XPATH, "//input[@data-test='@web/Search/SearchInput']").send_keys('coffee')
# Click search
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
# after clicks search will wait until page load to verify results --will not get critical errors
sleep(6)
# verify
expected_text = 'coffee'
actual_text = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
print(actual_text)
# asserts compares values assert 1==1 true
assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'

print('Test case passed')

