import pytest
from data import *
from selenium import webdriver
from pages.main_page import *

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.get(Urls.url)
    login = MainPage(driver)
    login.login()

    yield driver
    driver.quit()    