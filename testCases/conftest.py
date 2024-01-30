import pytest
from selenium import webdriver

@pytest.fixture
def settup():
    driver = webdriver.Edge()
    driver.maximize_window()
    return driver