import pytest
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск по локатору')
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Скрол до нужного элемента')    
    def scroll(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Ожидание видимости элемента')
    def wait_for_visibility(self, locator):
        return WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click(self, locator):
        self.find(locator).click()

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
        
    @allure.step('Ожидание видимости url')
    def wait_for_url(self, url):
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step('Получить текущий url')
    def get_current_url(self):
        return self.driver.current_url    

    @allure.step('Проверка невидимости элемента на странице')
    def check_invisibility(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.invisibility_of_element(locator))    

    @allure.step('Получение текста элемента')
    def get_text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Перетаскивание элемента')
    def drag_and_drop_element(self, locator_from, locator_to):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator_from))
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator_to))
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        self.driver.execute_script("""
                   var source = arguments[0];
                   var target = arguments[1];
                   var evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
               """, element_from, element_to)

 
    @allure.step('Клик по элементу при помощи js')
    def click_with_js(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)    

        