from selene import be
from selene.support.shared import browser
from appium.webdriver.common.appiumby import AppiumBy


def given_opened():
    if browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).matching(
            be.visible):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
