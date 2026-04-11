import pytest
import allure
from locators.main_page_locators import *
from locators.headers_locators import *
from locators.order_page_locators import *
from selenium.webdriver.common.keys import Keys
from data import *
from pages.base_page import *
class OrderPage(BasePage,):

    @allure.step('Клик по кнопке лента заказов')
    def click_order_button (self):
        return self.click(HeaderLocators.order_button)

    @allure.step('Получение количества заказов за все время')
    def check_counter_of_ingredients_all_time(self):
        return self.get_text_of_element(OrderPageLocators.orders_count_total) 

    @allure.step('Кдик по кнопке конструктор')
    def click_constructor_button(self):
        return self.click(HeaderLocators.constructor_button)

    @allure.step('Ожидаем открытие страницы конструктор')        
    def wait_for_url_costructor(self):
        return self.wait_for_url(Urls.url)  

    @allure.step('Ожидаем открытие страницы лента заказов')        
    def wait_for_url_order(self):
        return self.wait_for_url(Urls.orders_url)      

    @allure.step('Создание заказа и получение его номера')
    def make_order_and_get_order_number(self):
        self.drag_and_drop_element(locators.krator_bun, locators.order_basket)
        self.drag_and_drop_element(locators.spicy_sauce, locators.order_basket)
        self.click(locators.button_place_order)
        self.wait_for_visibility(locators.order_number)
        self.check_invisibility(locators.order_number_default)
        order_number = self.get_text_of_element(locators.order_number)
        self.click_with_js(locators.button_close_window)
        return order_number          

    @allure.step('Получение количества заказов за сегодня')
    def check_counter_of_ingredients_today(self):
        return self.get_text_of_element(OrderPageLocators.orders_count_today) 

    @allure.step('Получение номера заказа в работе')
    def check_number_order_in_work(self):
        return self.get_text_of_element(OrderPageLocators.order_in_work) 

    @allure.step('Ожидание надписи количество заказов за сегодня')
    def wait_for_counter_of_ingredients_today(self):    
        return self.wait_for_visibility(OrderPageLocators.text_orders_count_today)

    @allure.step('Ожидание надписи количество заказов за все время')
    def wait_for_counter_of_ingredients_total(self):
        return self.wait_for_visibility(OrderPageLocators.text_orders_count_total) 
    
    @allure.step('Ожидание кликабельности кнопки лента заказов')
    def wait_for_click_order_button (self):
        return self.wait_for_clickable(HeaderLocators.order_button)

    @allure.step('Клик по кнопке лента заказов js')
    def click_order_button_js (self):
        return self.click_with_js(HeaderLocators.order_button)    

    @allure.step('Ожидание надписи В работе')
    def wait_for_in_work(self):    
        return self.wait_for_visibility(OrderPageLocators.text_in_work)    

    @allure.step('Ожидание номера заказа в разделе В работе')
    def wait_for_number_of_order_in_work(self):    
        return self.wait_for_visibility(OrderPageLocators.order_in_work)      
    @allure.step('Ожидание исчезновения надписи "Все текущие заказы готовы" ')
    def check_invisible_all_orders_are_ready(self):    
        return self.check_invisibility(OrderPageLocators.all_orders_are_ready)    