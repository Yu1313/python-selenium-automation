from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


# open the url
driver.get('https://www.amazon.com/')

# Tags are first word in inspect window ex: div, input, span
# Attributes everything else after tags ex: type, id, autocomplete, class, dir

# Find element by ID
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'nav-logo-sprites')
# Find by Xpath
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
# Find by attribute only
driver.find_element(By.XPATH, "//*[@placeholder='Search Amazon']")
# find by multiple attributes
driver.find_element(By.XPATH, "//input[@tabindex='0' and @type= 'text' and @dir='auto']")
driver.find_element(By.XPATH, "//input[@tabindex='0' and @type= 'text']")

# Find search in dropdown locator
driver.find_element(By.XPATH, "//select[@aria-describedby= 'searchDropdownDescription' and @data-nav-selected= '0']")

# Find by text
driver.find_element(By.XPATH, "//a[text()='Amazon Basics']")
driver.find_element(By.XPATH, "//a[text()='Amazon Basics' and @class='nav-a  ']")

# connecting to parent node
driver.find_element(By.XPATH, "//div[@id='nav-main']//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//div[@id='nav-main']//a[contains(text(),'Best']")

# contains ** case sensitive
driver.find_element(By.XPATH, "//h2[contains(text(), 'under $30')]")



