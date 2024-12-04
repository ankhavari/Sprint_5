from selenium.webdriver.common.by import By

class LKProfile:
    PROFILE_NAV = (By.XPATH, "//a[contains(text(),'Профиль')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    ORDER_HISTORY = (By.XPATH, "//a[contains(text(),'История заказов')]")

class MainPage:
    LK_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]") # кнопка Личный кабинет на главной странице
    PLACE_ON_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")
    HEADER_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    HEADER_BUNS = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']")
    HEADER_SAUCE = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']")
    HEADER_FILLINGS = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']")
    BUNS_BUTTON = (By.XPATH, "//span[text()='Булки']")
    SAUCE_BUTTON = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_BUTTON = (By.XPATH, "//span[text()='Начинки']")

class AuthLogin:
    LOGIN_EMAIL = (By.XPATH, "//fieldset[1]//input[@class='text input__textfield text_type_main-default']")
    LOGIN_PASSWORD = (By.XPATH, "//fieldset[2]//input[@class='text input__textfield text_type_main-default']")
    LOGIN_HEADER = (By.XPATH, "//h2[contains(text(),'Вход')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    LOGIN_LINK_REGISTRATION_FORM = (By.XPATH, "//a[contains(text(),'Войти')]") # надпись Войти ссылкой

class AuthRegistration:
    REG_BUTTON = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")  # кнопка Зарегистрироваться на странице авторизации
    REG_AUTH_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    NAME = (By.XPATH, "//fieldset[1]//input[@class='text input__textfield text_type_main-default']") # инпут Имя
    REG_EMAIL = (By.XPATH, "//fieldset[2]//input[@class='text input__textfield text_type_main-default']") # инпут Email
    REG_PASSWORD = (By.XPATH, "//fieldset[3]//input[@class='text input__textfield text_type_main-default']") # инпут Пароль
    ERROR_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default']")