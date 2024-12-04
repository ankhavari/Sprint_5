from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Constants
from locators import *

class TestConstructorPage:
    def test_go_to_constructor_by_button(self, driver, login):
        # Проверка перехода к конструктору по нажатию на кнопку Конструктор

        driver.find_element(*MainPage.LK_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(LKProfile.PROFILE_NAV))
        driver.find_element(*MainPage.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.CONSTRUCTOR_HEADER))
        assert driver.find_element(*MainPage.CONSTRUCTOR_HEADER).text == 'Соберите бургер'

    def test_go_to_constructor_by_logo(self, driver, login):
        # Проверка перехода к конструктору по нажатию на логотип

        driver.find_element(*MainPage.LK_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(LKProfile.PROFILE_NAV))
        driver.find_element(*MainPage.HEADER_LOGO).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.CONSTRUCTOR_HEADER))
        assert driver.find_element(*MainPage.CONSTRUCTOR_HEADER).text == 'Соберите бургер'

    def test_go_to_sauces(self, driver, login):
        # Проверка перехода к разделу Соусы
        driver.find_element(*MainPage.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*MainPage.SAUCE_BUTTON).click()
        assert driver.find_element(*MainPage.HEADER_SAUCE).text == 'Соусы'

    def test_go_to_fillings(self, driver, login):
        # Проверка перехода к разделу Начинки
        driver.find_element(*MainPage.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*MainPage.FILLINGS_BUTTON).click()
        assert driver.find_element(*MainPage.HEADER_FILLINGS).text == 'Начинки'

    def test_go_to_buns(self, driver, login):
        # Проверка перехода к разделу Булки
        driver.find_element(*MainPage.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*MainPage.FILLINGS_BUTTON).click()
        driver.find_element(*MainPage.BUNS_BUTTON).click()
        assert driver.find_element(*MainPage.HEADER_BUNS).text == 'Булки'