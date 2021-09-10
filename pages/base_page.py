from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(15)
        self.category_text = ''
        self.prev_image = ''

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def get_category_text(self):
        return self.category_text

    def set_category_text(self, text):
        self.category_text = text

    def get_prev_image(self):
        return self.prev_image

    def set_prev_image(self, image):
        self.prev_image = image
