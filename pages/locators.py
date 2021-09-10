from selenium.webdriver.common.by import By


class MainPageLocators:
    INPUT_FIELD = (By.CSS_SELECTOR, "#text")
    SUGGEST_TABLE = (By.CSS_SELECTOR, "div.mini-suggest__popup_visible")
    IMAGE_URL = (By.CSS_SELECTOR, "ul.services-new__list li:nth-child(3)")


class SearchPageLocators:
    LINK_FIRST = (By.CSS_SELECTOR, 'li.serp-item a.link_theme_outer b')
    LINKS = (By.CSS_SELECTOR, 'li.serp-item a.Link_theme_outer b')
    INPUT_FIELD = (By.CSS_SELECTOR, 'input.input__control')
    FIRST_IMAGE = (By.CSS_SELECTOR, 'a.serp-item__link')
    IMAGE = (By.CSS_SELECTOR, '.MMImage-Origin')
    FORWARD_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_next')
    BACK_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_prev')


class ImagesPageLocators:
    FIRST_CATEGORY = (By.CSS_SELECTOR, 'div.PopularRequestList-SearchText')
