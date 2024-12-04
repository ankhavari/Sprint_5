import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Constants
from locators import *

class TestRegistration:
    def test_registration_successful_registration(self, driver):
        # Проверка успешной регистрации
        driver.get(Constants.URL_REG)
        driver.find_element(*AuthRegistration.NAME).send_keys(Constants.NAME)
        driver.find_element(*AuthRegistration.REG_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*AuthRegistration.REG_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*AuthRegistration.REG_AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AuthLogin.LOGIN_HEADER))
        assert driver.current_url == Constants.URL_LOGIN and driver.find_element(*AuthLogin.LOGIN_BUTTON).text == 'Войти'

    def test_incorrect_password_error_registration(self, driver):
        # Проверка отображения ошибки для некорректного пароля
        driver.get(Constants.URL_REG)
        driver.find_element(*AuthRegistration.NAME).send_keys(Constants.NAME)
        driver.find_element(*AuthRegistration.REG_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*AuthRegistration.REG_PASSWORD).send_keys('123')
        driver.find_element(*AuthRegistration.REG_AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(AuthRegistration.ERROR_MESSAGE))
        assert driver.find_element(*AuthRegistration.ERROR_MESSAGE).text == 'Некорректный пароль'