from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Constants
from locators import *

class TestLogout:
    def test_logout_show_login_form(self, driver, login):
        # Выход из аккаунта

        driver.find_element(*MainPage.LK_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(LKProfile.PROFILE_NAV))
        driver.find_element(*LKProfile.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AuthLogin.LOGIN_HEADER))
        assert driver.current_url == Constants.URL_LOGIN and driver.find_element(*AuthLogin.LOGIN_BUTTON).text == 'Войти'