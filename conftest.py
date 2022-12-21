import os
import pytest
from appium import webdriver
from dotenv import load_dotenv
from selene.support.shared import browser
from assist.attach import *


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    load_dotenv()
    options = {
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        "app": "bs://8d59ebf677534789e16e08a37a7e86d112279c88",
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-DEMO",
            "sessionName": "BStack first_test"
        }
    }
    USER_NAME = os.getenv('user_name')
    ACCESS_KEY = os.getenv('access_key')
    browser.config.driver = webdriver.Remote(
        command_executor=f"https://{USER_NAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=options
    )
    browser.config.timeout = 4
    yield setup_browser
    add_video(browser)
    screenshot(browser)
    screen_xml_dump(browser)
    screen_html_dump(browser)
    browser.quit()
