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

# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('table')

# wait for 4 sec
sleep(4)

# click search button
driver.find_element(By.NAME, 'btnK').click()

# verify search results
assert 'table' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
