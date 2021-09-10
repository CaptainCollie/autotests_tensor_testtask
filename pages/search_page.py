from .base_page import BasePage
from .locators import SearchPageLocators


class SearchPage(BasePage):
    def should_be_in_first_five(self):
        links = [self.browser.find_element(*SearchPageLocators.LINK_FIRST)] + self.browser.find_elements(
            *SearchPageLocators.LINKS)[:4]
        links = [i.text for i in links]
        assert 'tensor.ru' in links, "There is no 'tensor.ru' in first five links"

    def should_be_image_search_page(self):
        assert 'search' in self.browser.current_url, 'It is not search page'

    def should_be_right_text_in_input_field_after_images_category(self):
        assert self.category_text == self.browser.find_element(
            *SearchPageLocators.INPUT_FIELD).text, 'Wrong text in input field'

    def should_be_image(self):
        assert self.is_element_present(*SearchPageLocators.IMAGE), 'Image did not opened'

    def should_be_another_image(self):
        assert self.prev_image != self.browser.find_element(*SearchPageLocators.IMAGE).get_attribute(
            'src'), 'Image is same'

    def should_be_same_image(self):
        assert self.prev_image == self.browser.find_element(*SearchPageLocators.IMAGE).get_attribute(
            'src'), 'Image is different'

    def click_on_first_image(self):
        self.browser.find_element(*SearchPageLocators.FIRST_IMAGE).click()

    def click_forward_button(self):
        self.set_prev_image(self.browser.find_element(*SearchPageLocators.IMAGE).get_attribute('src'))
        self.browser.find_element(*SearchPageLocators.FORWARD_BUTTON).click()

    def click_back_button(self):
        self.browser.find_element(*SearchPageLocators.BACK_BUTTON).click()
