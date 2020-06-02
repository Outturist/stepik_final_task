from .base_page import BasePage
from .locators import ProductPageLoacators


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        self.add_to_basket()
        self.should_be_success_alert()
        self.should_be_right_name_of_the_added_book_in_alert()
        self.should_be_alert_with_basket_cost()
        self.should_be_equal_book_price_and_cost_in_alert()

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLoacators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_success_alert(self):
        assert self.is_element_present(*ProductPageLoacators.SUCCSESS_ALERT_ADDED_TO_BASKET), "There isn't success alert"

    def should_be_right_name_of_the_added_book_in_alert(self):
        book_name = self.browser.find_element(*ProductPageLoacators.BOOK_NAME).text
        book_name_in_allert = self.browser.find_element(*ProductPageLoacators.BOOK_NAME_IN_ALLERT).text
        assert book_name == book_name_in_allert, f"book name in allert isn't right, expected: {book_name}, appeared: {book_name_in_allert}"

    def should_be_alert_with_basket_cost(self):
        assert self.is_element_present(
            *ProductPageLoacators.ALERT_WITH_BASKET_COST), "There isn't alert_with_basket_cost"

    def should_be_equal_book_price_and_cost_in_alert(self):
        cost_in_alert = self.browser.find_element(*ProductPageLoacators.COST_IN_ALERT).text
        book_price = self.browser.find_element(*ProductPageLoacators.BOOK_PRICE).text
        assert cost_in_alert == book_price, f"cost in alert isn't the same as book price, expected: {book_price}, appeared: {cost_in_alert}"

    def should_not_be_success_message_after_opening_product_page(self):
        assert self.is_not_element_present(*ProductPageLoacators.SUCCSESS_ALERT_ADDED_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_after_adding_product_to_basket_is_not_element_present(self):
        assert self.is_not_element_present(*ProductPageLoacators.SUCCSESS_ALERT_ADDED_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_after_adding_product_to_basket_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLoacators.SUCCSESS_ALERT_ADDED_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_be_login_url(self):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        url = self.browser.current_url
        assert url == link, f'Login link is {url}, expected {link}'
