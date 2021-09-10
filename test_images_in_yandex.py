from .pages.main_page import MainPage
from .pages.search_page import SearchPage
from .pages.images_page import ImagesPage
import pytest


class TestImagesInYandex:
    def test_images_in_yandex(self, browser):
        link = 'https://yandex.ru/'
        page = MainPage(browser, link)
        page.open()
        page.should_be_image_url()
        page.click_on_image_url()

        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)

        images_page = ImagesPage(browser, browser.current_url)
        images_page.should_be_images_page()
        images_page.click_on_first_category()

        search_page = SearchPage(browser, browser.current_url)
        search_page.should_be_image_search_page()
        search_page.should_be_right_text_in_input_field_after_images_category()
        search_page.click_on_first_image()
        search_page.should_be_image()
        search_page.click_forward_button()
        search_page.should_be_another_image()
        search_page.click_back_button()
        search_page.should_be_same_image()

