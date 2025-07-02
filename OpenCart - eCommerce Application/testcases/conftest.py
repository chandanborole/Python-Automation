# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     return driver
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver