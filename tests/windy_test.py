from unittest import TestCase

import allure
import pytest
from selene.api import *
from selene.browsers import BrowserName


class TestWindyApp(TestCase):
    def setUp(self):
        config.browser_name = BrowserName.CHROME
        browser.open_url('https://www.windy.com/')
        config.reports_folder = "screenshots"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("Menu.")
    @allure.testcase("Windy burger menu works correct.")
    def test_menu_burger(self):
        s('#menu-burger2').should(be.visible).click()
        s('div.rhpane-menu').should(be.visible)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("Search.")
    @allure.testcase("Search location and check weather pop-up.")
    def test_search_city_weather(self):
        location = "Lviv International Airport"
        # Search location weather
        s('#q').should(be.visible).set(location).press_enter()
        # Click on first search result
        ss('div.results > div > a')[0].click()
        # Validate proper detailed weather opened.
        # Open related popup tab.
        s('#plugin-airport').s('div[data-do="set,info"]').click()
        s('div.section-title').should(have.exact_text(location))

    def tearDown(self):
        browser.close()
