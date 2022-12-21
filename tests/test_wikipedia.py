from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from allure import step

from wikipedia_mobile.model import app


def test_search():
    app.given_opened()

    with step('Search for content'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(
            'BrowserStack'
        )

    with step('Content should be found'):
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).should(have.size_greater_than(0))


def test_getting_started():
    with step('Title should be visible'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')) \
            .should(have.text('The Free Encyclopedia'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Title should be visible'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')) \
            .should(have.text('New ways to explore'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Title should be visible'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')) \
            .should(have.text('Reading lists with sync'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Title should be visible'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')) \
            .should(have.text('Send anonymous data'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()

    with step('Search should be found'):
        browser.all(
            (AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')
        ).should(have.size_greater_than(0))


def test_settings():
    app.given_opened()

    with step('Open settings'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/menu_icon')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/main_drawer_settings_container')).click()

    with step('Content should be found'):
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/action_bar')
        ).element((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text('Settings'))


def test_customise():
    app.given_opened()

    with step('Click customize'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_announcement_action_positive')).click()

    with step('Content should be found'):
        assert browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/action_bar')
        ).element((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text('Customize the feed'))


def test_find_nothing():
    app.given_opened()

    with step('Search for content'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(
            'qsdiddCсвцЦап[ued'
        )

    with step('Content should not be found'):
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).should(have.size(0))