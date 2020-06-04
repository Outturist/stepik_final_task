from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):

    def should_not_be_goods_in_the_basket(self):
        assert self.is_not_element_present(*BasePageLocators.GOODS_IN_THE_BASKET), \
            "Goods is presented in basket, but should not be"

    def should_be_text_your_basket_is_empty(self):
        assert self.is_element_present(*BasePageLocators.YOUR_BASKET_IS_EMPTY_TEXT), \
            'Text "Your basket is empty" absent in basket, but should be'

