from .base_page import BasePage
from .locators import ImagesPageLocators


class ImagesPage(BasePage):

    def should_be_images_page(self):
        assert 'https://yandex.ru/images/' in self.browser.current_url, 'It is not images page'

    def click_on_first_category(self):
        text = self.browser.find_element(*ImagesPageLocators.FIRST_CATEGORY).text
        self.set_category_text(text)
        self.browser.find_element(*ImagesPageLocators.FIRST_CATEGORY).click()


