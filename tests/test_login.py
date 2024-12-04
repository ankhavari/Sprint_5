from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Constants
from locators import *

class TestLogin:
    def test_login_via_login_to_account_button_show_main_page(self, driver):
        # Проверка входа по кнопке «Войти в аккаунт» на главной

        driver.find_element(*MainPage.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthLogin.LOGIN_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*AuthLogin.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*AuthLogin.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.PLACE_ON_ORDER_BUTTON))
        assert driver.current_url == Constants.URL and driver.find_element(*MainPage.PLACE_ON_ORDER_BUTTON).text == 'Оформить заказ'

    def test_login_via_lk_button_show_main_page(self, driver):
        # Проверка входа через кнопку «Личный кабинет»

        driver.find_element(*MainPage.LK_BUTTON).click()
        driver.find_element(*AuthLogin.LOGIN_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*AuthLogin.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*AuthLogin.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.PLACE_ON_ORDER_BUTTON))
        assert driver.current_url == Constants.URL and driver.find_element(*MainPage.PLACE_ON_ORDER_BUTTON).text == 'Оформить заказ'

    def test_login_via_button_in_registration_form_show_main_page(self, driver):
        # Проверка входа через кнопку в форме регистрации

        driver.find_element(*MainPage.LK_BUTTON).click()
        driver.find_element(*AuthRegistration.REG_BUTTON).click()
        driver.find_element(*AuthLogin.LOGIN_LINK_REGISTRATION_FORM).click()
        driver.find_element(*AuthLogin.LOGIN_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*AuthLogin.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*AuthLogin.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.PLACE_ON_ORDER_BUTTON))
        assert driver.current_url == Constants.URL and driver.find_element(*MainPage.PLACE_ON_ORDER_BUTTON).text == 'Оформить заказ'


    def test_login_via_password_recovery_form_show_main_page(self, driver):
        # Проверка входа через кнопку в форме восстановления пароля

        driver.find_element(*MainPage.LK_BUTTON).click()
        driver.find_element(*AuthLogin.RECOVER_PASSWORD_LINK).click()
        driver.find_element(*AuthLogin.LOGIN_LINK_REGISTRATION_FORM).click()
        driver.find_element(*AuthLogin.LOGIN_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*AuthLogin.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*AuthLogin.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.PLACE_ON_ORDER_BUTTON))
        assert driver.current_url == Constants.URL and driver.find_element(*MainPage.PLACE_ON_ORDER_BUTTON).text == 'Оформить заказ'