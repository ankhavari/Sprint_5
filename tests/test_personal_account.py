from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Constants
from locators import *

class TestPersonalAccount:
    def test_go_to_personal_account_open_profile(self, driver, login):
        driver.find_element(*MainPage.LK_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(LKProfile.PROFILE_NAV))
        history = driver.find_element(*LKProfile.ORDER_HISTORY)
        assert driver.current_url == Constants.URL_PROFILE and history.text == 'История заказов'