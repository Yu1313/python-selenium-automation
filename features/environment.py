from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  #alias to make this short in code
from time import sleep
from app.application import Application


def browser_init(context, scenario_name): # function used to start browser
    """
    :param context: Behave context
    """
    # Running test parallel separately. Chrome daily, safari release only
    # if 'browser' in os.environ:
    #     if os.environ:['browser'] == 'chrome'        # automation launched by ci service, each job trigger config
    #        driver_path = ChromeDriverManager().install()
    #        service = Service(driver_path)
    #        context.driver = webdriver.Chrome(service=service)
    #     elif os.environ:['browser'] == 'ff'          # automation launched by ci service, each job trigger config
    #           driver_path = GeckoDriverManager().install()
    #           service = Service(driver_path)
    #           context.driver = webdriver.Firefox(service=service)
    driver_path = './chromedriver.exe' # for windows users
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)  # define browser used

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # context.driver = webdriver.Safari()       # define browser used

    ### BROWSERS WITH DRIVERS: provide path to the driver file ###
    # service = Service(executable_path='/Users/svetlanalevinsohn/careerist/19-python-selenium-automation/geckodriver')
    # context.driver = webdriver.Firefox(service=service)

    ### SAFARI ###
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    # ### BROWSERSTACK ###
    # # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'yus_v62daS'
    # bs_key = 'V2UYdzzPtNCZJUCxB5qW'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'OS X',
    #     'osVersion': 'Ventura',
    #     'browserName': 'Safari',
    #     "browserVersion": "16.5",
    #     "seleniumVersion": "4.21.0",
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):  # called hooks
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
