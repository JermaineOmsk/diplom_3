import allure
from pages.main_page import *
from data import Urls


class TestHeaderPage:
    @allure.title('Проверка перехода в "Конструктор"')
    def test_redirect_to_constructor(self, driver):
        constructor_button = MainPage(driver)
        constructor_button.click_order_button()
        constructor_button.click_constructor_button()
        constructor_button.wait_for_url_costructor()
        current_url = constructor_button.get_current_url()
        assert current_url == Urls.url

    @allure.title('Проверка перехода в "Лента зказазов"')
    def test_redirect_to_orders(self, driver):
        orders_button = MainPage(driver)
        orders_button.click_order_button()
        orders_button.wait_for_url_orders()
        current_url = orders_button.get_current_url()
        assert current_url == Urls.orders_url

class TestMainPage: 
    @allure.title('Проверка появления всплывающего окна с деталями при клике на ингридиент')
    def test_popup_window_with_details(self, driver):
        popup = MainPage(driver)
        popup.click_flu_bun()
        popup.wait_for_popup_details_ingredients()
        details_window = popup.find_popup_details_window()
        assert details_window.is_displayed()

    @allure.title('Проверка закрытия всплывающего окна с деталями ингридиента кликом на крестик')
    def test__close_popup_window_with_details_using_cross(self, driver):
        popup = MainPage(driver)
        popup.click_flu_bun()
        popup.wait_for_popup_details_ingredients()
        popup.click_popup_details_window_cross()
        popup.check_invisible_popup_details_ingredients()
        details_window = popup.find_popup_details_window()
        assert details_window.is_displayed() is False        

    @allure.title('Проверка изменения счетчика ингредиента')
    def test_change_ingredient_counter(self, driver):
        ingredient = MainPage(driver)
        ingredient.add_filling_to_order_basket()
        ingredient.wait_for_ingredient__count_raise
        quantity = ingredient.check_counter_of_ingredients()
        assert quantity == "1"
    