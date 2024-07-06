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

# css selector syntax $$("")

# Find By css ID (tag is optional and goes in the beginning ex. tag#id)
driver.find_element(By. CSS_SELECTOR, "#twotabsearchtextbox")
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox") # tag and id

# Find by css classes: classes are separated by space ex: nav-input nav-progressive-attribute are 2 different classes
# order does not matter last class can come before first, can use tag in beginning tag.class
# .class
driver.find_element(By.CSS_SELECTOR, ".nav-input")
# multiple class class2.class1
driver.find_element(By.CSS_SELECTOR, ".nav-progressive-attribute.nav-input")
driver.find_element(By.CSS_SELECTOR, ".nav-a.a-popover-trigger")
# tag + class
driver.find_element(By.CSS_SELECTOR, "input.nav-progressive-attribute.nav-input")
# tag + id + classes can add as many classes needed
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-progressive-attribute.nav-input")
# Attributes
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")  # attribute
# multiple attribute: narrow search connect to particular element-- achievable by multiple attribute
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon'][type='text']")
driver.find_element(By.CSS_SELECTOR, "[tabindex='0']'][type='text']")
# tag + attribute
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon'][type='text']")
# tag + #id + .class + [attributes]
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input[placeholder='Search Amazon']")
# Attributes, partial match [attribute*='partial value'] note class is also attribute
driver.find_element(By.CSS_SELECTOR, "[placeholder*='earch Ama']")
driver.find_element(By.CSS_SELECTOR,"a[href*='ap_signin_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR,"[class*='ap_signin_notification_privacy_notice']")

# Multiple nodes parent => child space before attribute/class doesnt have to be direct parent could be further up chain
driver.find_element(By.CSS_SELECTOR,"div#legalTextRow [href*='ap_signin_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR,"div [href*='ap_signin_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR,"div.a-box div#legalTextRow [href*='condition']")

# Side Note
# Old projects written by people dont know css would use XPATHS
# Order, ID, CSS Selector, XPATH
# ***CSS SELECTORS Do not support Text***
# CSS Selectors can only go top down parent to child, xpath can go child to parent
# css selector is faster than xpath


