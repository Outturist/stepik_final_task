from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLoacators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    SUCCSESS_ALERT_ADDED_TO_BASKET = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-success  fade in"][1]')
    ALERT_WITH_BASKET_COST = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-info  fade in"]')
    COST_IN_ALERT = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-info  fade in"]//p/strong')
    BOOK_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]//h1')
    BOOK_NAME_IN_ALLERT = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-success  fade in"][1]//div//strong')
    BOOK_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]//p[@class="price_color"]')

