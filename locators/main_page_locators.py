from selenium.webdriver.common.by import By
class locators:    
    
    create_burger_logo = (By.XPATH, '//h1[text()="Соберите бургер"]')  # заголовок "Соберите бургер"
    button_log_in_account = (By.XPATH, '//button[text()="Войти в аккаунт"]') #кнопка "войти в аккаунт"
    button_place_order = (By.XPATH, '//button[text()="Оформить заказ"]') #кнопка "оформить заказ" 
    span_to_sauce = (By.XPATH, '//span[text() = "Соусы"]')#прокрутить до соусов
    span_to_topping = (By.XPATH, '//span[text() = "Начинки"]')#прокрутить до начинок
    span_to_bread = (By.XPATH, '//span[text() = "Булки"]')#прокрутить до булочек
    text_bread = (By.XPATH, "//h2[text()='Булки']") # надпись Булки
    text_sauce = (By.XPATH, "//h2[text()='Соусы']") # надпись Соусы
    text_topping= (By.XPATH, "//h2[text()='Начинки']") # надпись Начинки
    button_log_in_account = (By.XPATH, '//button[text()="Войти в аккаунт"]') #кнопка "войти в аккаунт"
    create_order_button = (By.XPATH, '//button[text()="Оформить заказ"]')  # кнопка "Оформить заказ"
    krator_bun = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]')  # краторная булка
    flu_bun = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]')#флю булка
    space_sauce = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]')  # space sauce
    spicy_sauce = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]')  # Spicy-X sauce
    spicy_sauce_count = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]//p[contains(@class, "counter__num")]') # Spicy-X sauce счетчик
    traditional_sauce = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa74"]')  # traditional sauce
    protostomia_filling = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]')  # protostomia
    beef_meteor_filling = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa70"]')  # beef_meteor
    window_details_of_ingredients = (By.XPATH, '//h2[text()="Детали ингредиента"]')  # заголовок всплывающего окна "Детали ингредиента"
    ingredient_popup = (By.XPATH, '//*[contains(@class, "contentBox")]')  # всплывающее окно "Детали ингредиента"
    order_basket = (By.XPATH, '//ul[contains(@class,"BurgerConstructor_basket")]')  # корзина заказа
    order_number = (By.XPATH, '//*[contains(@class, "type_digits-large")]')  # номер заказа во всплывающем окне
    order_number_default = (By.XPATH, '//h2[text()="9999"]')  # номер заказа по умолчанию во всплывающем окне
    order_status_text = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')  # "Ваш заказ начали готовить" в всплывающем окне
    button_close_window = (By.XPATH, '//button[contains(@class,"close")]')  # кнопка закрытия всплывающего окна
    krator_bun_counter = (By.XPATH, ('//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]//p[contains(@class, '
                                    '"counter__num")]'))  # счетчик ингредиента "Краторная булка N-200i"
    bun_bottom_basket = (By.XPATH, '//*[contains(@class, "constructor-element constructor-element_pos_bottom")]')
                         