import allure
from pages.order_page import *
from data import *
import time
class TestOrderPage:

    @allure.title('Проверка появления номера зказа в разделе "В работе"')
    def test_number_of_order_in_order_in_work(self, driver):
        order = OrderPage(driver)
        order_number = order.make_order_and_get_order_number()
        order.wait_for_click_order_button()
        order.click_order_button_js()
        order.wait_for_url_order()
        order.wait_for_in_work()
        order.check_invisible_all_orders_are_ready()
        order.wait_for_number_of_order_in_work()
        order_number_in_work = order.check_number_order_in_work()
        assert (f'0{order_number}') == order_number_in_work  


    @allure.title('Проверка при создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    def test_count_of_orders_all_time(self, driver):
        order = OrderPage(driver)
        order.click_order_button()
        order.wait_for_url_order()
        order.wait_for_counter_of_ingredients_total()
        count = order.check_counter_of_ingredients_all_time()
        order.click_constructor_button()
        order.wait_for_url_costructor()
        order.make_order_and_get_order_number()
        order.wait_for_click_order_button()
        order.click_order_button_js()
        order.wait_for_url_order()
        order.wait_for_counter_of_ingredients_total()
        count_after = order.check_counter_of_ingredients_all_time()
        assert count_after > count


    @allure.title('Проверка при создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_count_of_orders_today(self, driver):
        order = OrderPage(driver)
        order.click_order_button()
        order.wait_for_url_order()
        order.wait_for_counter_of_ingredients_today()
        count = order.check_counter_of_ingredients_today()
        order.click_constructor_button()
        order.wait_for_url_costructor()
        order.make_order_and_get_order_number()
        order.wait_for_click_order_button()
        order.click_order_button_js()
        order.wait_for_url_order()
        order.wait_for_counter_of_ingredients_today()
        count_after = order.check_counter_of_ingredients_today()
        assert count_after > count    


      