from selenium.webdriver.common.by import By
class OrderPageLocators:
    order_feed_logo = (By.XPATH, '//h1[text()="Лента заказов"]')  # заголовок "Лента заказов"
    order_link = (By.XPATH, '//*[contains(@class, "OrderHistory_link")]')  # ссылка на заказ в списке "Лента заказа"
    content_order_logo = (By.XPATH, '//p[text()="Cостав"]')  # заголовок "Состав" в окне с деталями заказа
    order_number = By.XPATH, '//p[text()="{}"]'  # номер заказа из списка "Лента заказов"
    all_orders_are_ready = (By.XPATH, '//li[text()="Все текущие заказы готовы!"]')  # текст "Все текущие заказы готовы!"
    order_in_work = (By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]') ## номер заказа в работе
    orders_count_today = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p[1]")  # количество заказов выполненных сегодня
    orders_count_total = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p[1]")  # количество заказов выполненных за всё время
    text_orders_count_total = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]")
    text_orders_count_today = (By.XPATH, "//p[text()='Выполнено за сегодня:']")
    text_in_work = (By.XPATH, "//p[contains(text(), 'В работе')]")
