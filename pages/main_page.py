from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    def should_be_input_field(self):
        assert self.is_element_present(*MainPageLocators.INPUT_FIELD), 'There is no input field'

    def send_keys_in_input_field(self, query):
        input_field = self.browser.find_element(*MainPageLocators.INPUT_FIELD)
        input_field.send_keys(query)

    def should_be_suggest_table(self):
        assert self.is_element_present(*MainPageLocators.SUGGEST_TABLE), 'There is no suggest table'

    def should_be_image_url(self):
        assert self.is_element_present(*MainPageLocators.IMAGE_URL), 'There is no image url'

    def click_on_image_url(self):
        self.browser.find_element(*MainPageLocators.IMAGE_URL).click()

    def press_enter(self):
        self.browser.find_element(*MainPageLocators.INPUT_FIELD).send_keys(Keys.ENTER)