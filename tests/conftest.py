import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import *

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Constants.URL)
    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*MainPage.LOGIN_TO_ACCOUNT_BUTTON).click()
    driver.find_element(*AuthLogin.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*AuthLogin.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*AuthLogin.LOGIN_BUTTON).click()
    return driver