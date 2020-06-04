from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GOODS_IN_THE_BASKET = (By.XPATH, '//div[@class="basket-items"]')
    YOUR_BASKET_IS_EMPTY_TEXT = (By.XPATH, '//div[@id="content_inner"]//p[contains(.,"Your basket is empty")]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET_BUTTON = (By.XPATH, '//a[@class="btn btn-default"]')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_FIELD = (By.XPATH, '//input[@name="registration-email"]')
    REGISTRATION_PASSWORD_FIELD = (By.XPATH, '//input[@name="registration-password1"]')
    CONFIRM_PASSWORD_FIELD = (By.XPATH, '//input[@name="registration-password2"]')
    REGISTRATION_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLoacators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    SUCCSESS_ALERT_ADDED_TO_BASKET = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-success  fade in"][1]')
    ALERT_WITH_BASKET_COST = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-info  fade in"]')
    COST_IN_ALERT = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-info  fade in"]//p/strong')
    BOOK_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]//h1')
    BOOK_NAME_IN_ALLERT = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-success  fade in"][1]//div//strong')
    BOOK_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]//p[@class="price_color"]')

