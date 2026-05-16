from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    enter = (By.XPATH, "//h2[text()='Вход']") #Надпись вход
    email = (By.XPATH, "//label[text()='Email']/following-sibling::input") #поле мыло    
    password = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") #поле пароль
    button_enter = (By.XPATH, '//button[text()="Войти"]') #кнопка "войти" 