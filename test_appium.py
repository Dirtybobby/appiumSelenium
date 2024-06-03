import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

@pytest.fixture()
def driver():
    app_driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield app_driver
    if driver:
        app_driver.quit()



def test_find_battery(driver):
    el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    el.click()
    sleep(5)

