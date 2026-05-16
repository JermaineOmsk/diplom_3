import pytest
import allure
from locators.main_page_locators import *
from locators.headers_locators import *
from locators.main_page_locators import *
from locators.personal_account_locators import *
from selenium.webdriver.common.keys import Keys
from data import *
from pages.base_page import *
class MainPage(BasePage,):

   
    @allure.step('Клик по кнопке конструктор')
    def click_constructor_button(self):
        return self.click(HeaderLocators.constructor_button)

    @allure.step('Кдик по кнопке лента заказов')    
    def click_order_button (self):
        return self.click(HeaderLocators.order_button)

    @allure.step('Ожидаем открытие страницы конструктор')  
    def wait_for_url_costructor(self):
        return self.wait_for_url(Urls.url)

    @allure.step('Ожидаем урл ленты заказов')
    def wait_for_url_orders(self):
        return self.wait_for_url(Urls.orders_url)    

    @allure.step('Клик по флюорисцентной булочки')
    def click_flu_bun(self):
        return self.click(locators.flu_bun) 

    @allure.step('Ожидаем появление окна с деталями ингридиентов')
    def wait_for_popup_details_ingredients(self):    
        return self.wait_for_visibility(locators.window_details_of_ingredients)

    @allure.step('Поиск всплывающего окна с деталями ингридиентов')
    def find_popup_details_window(self):
        return self.find(locators.window_details_of_ingredients)   
    @allure.step('Клик по крестику')
    def click_popup_details_window_cross(self):
        return self.click(locators.button_close_window )
    @allure.step('Проверка что всплывающее окно с деталями ингредиентов закрыто')
    def check_invisible_popup_details_ingredients(self):    
        return self.check_invisibility(locators.window_details_of_ingredients)

    @allure.step('Получение количества добавленного ингредиента спайси соус')
    def check_counter_of_ingredients(self):
        return self.get_text_of_element(locators.spicy_sauce_count)    

    @allure.step('Добавление начинки спайси соус в корзину')
    def add_filling_to_order_basket(self):
        return self.drag_and_drop_element(locators.spicy_sauce , locators.order_basket)

    @allure.step('Ожидание увеличения счетчика ингредиента')
    def wait_for_ingredient__count_raise(self):    
        return self.wait_for_visibility(locators.spicy_sauce_count)

    @allure.step('Создание заказа и получение его номера')
    def make_order_and_get_order_number(self):
        self.drag_and_drop_element(locators.krator_bun, locators.order_basket)
        self.drag_and_drop_element(locators.spicy_sauce, locators.order_basket)
        self.click(locators.button_place_order)
        self.wait_visibility_element(locators.order_number_default)
        self.wait_invisibility_element(locators.order_number)
        order_number = self.get_text_of_element(locators.order_number)
        self.click(locators.button_close_window)
        return order_number

    
    @allure.step('Вход в личный кабинет')
    def login(self):
        self.find(HeaderLocators.button_personal_account)
        self.click(HeaderLocators.button_personal_account)
        self.wait_for_visibility(PersonalAccountLocators.enter)
        self.find(PersonalAccountLocators.email).send_keys(User.mail)
        self.find(PersonalAccountLocators.password).send_keys(User.valid_password)
        self.find(PersonalAccountLocators.button_enter)
        self.click(PersonalAccountLocators.button_enter)
        self.wait_for_visibility(locators.button_place_order)