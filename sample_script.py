from selenium import webdriver  # allows pycharm to work with selenium elements
from selenium.webdriver.common.by import By  # allows pycharm to work with selenium locators
from selenium.webdriver.chrome.service import Service      # allows selenium to connect with chrome
from webdriver_manager.chrome import ChromeDriverManager  # allows selenium to connect with chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  #alias to make this short in code
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()    # connects to  chrome

# create a new Chrome browser instance
service = Service(driver_path)  # starts chrome
driver = webdriver.Chrome(service=service)  # starts chrome
driver.maximize_window()  # maximizes Chrome browser screen
driver.implicitly_wait(5)
driver.wait = WebDriverWait(driver, 15)   #typically will se 10 or 15
# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('table')

# wait for 4 sec changed to implicit wait


# click search button
driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK'))).click()

# verify search results
assert 'table' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
