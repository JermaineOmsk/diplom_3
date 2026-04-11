import pytest
from data import *
from selenium import webdriver
from locators.headers_locators import *
from locators.personal_account_locators import *
from locators.main_page_locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.get(Urls.url)
    driver.find_element(*HeaderLocators.button_personal_account).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.enter))
    driver.find_element(*PersonalAccountLocators.email).send_keys(User.mail)
    driver.find_element(*PersonalAccountLocators.password).send_keys(User.valid_password)
    driver.find_element(*PersonalAccountLocators.button_enter).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.button_place_order))

    yield driver
    driver.quit()    