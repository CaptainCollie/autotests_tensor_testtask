from .pages.main_page import MainPage
from .pages.search_page import SearchPage
import pytest


class TestSearchInYandex:
    def test_search_in_yandex(self, browser):
        link = 'https://yandex.ru/'
        page = MainPage(browser, link)
        page.open()
        page.should_be_input_field()
        page.send_keys_in_input_field('тензор')
        page.should_be_suggest_table()
        page.press_enter()
        search_page = SearchPage(browser, browser.current_url)
        search_page.should_be_in_first_five()
