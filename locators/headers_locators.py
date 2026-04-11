from selenium.webdriver.common.by import By
class HeaderLocators:
    constructor_button = (By.XPATH, "//p[text()='Конструктор']")
    order_button = (By.XPATH, "//p[text()='Лента Заказов']")
    button_personal_account = (By.XPATH, '//p[text() = "Личный Кабинет"]')