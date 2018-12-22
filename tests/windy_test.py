from selene.browsers import BrowserName
from selene.api import *
from unittest import TestCase
import time


class TestWindyApp(TestCase):
    def setUp(self):
        config.browser_name = BrowserName.CHROME
        browser.open_url('https://www.windy.com/')
        config.reports_folder = "selene_reports"

    def test_menu_burger(self):
        s('#menu-burger2').should(be.visible).click()
        s('div.rhpane-menu').should(be.visible)

    def test_search_city_weather(self):
        city = "Lviv"
        # Search city weather
        s('#q').should(be.visible).set(city).press_enter()
        # Click on first search result
        ss('div.results > div > a')[0].click()
        # Validate proper detailed weather opened
        s('div.stations-container.content-container').should(have.text(city))
