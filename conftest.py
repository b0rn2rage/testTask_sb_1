import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--baseurl", default="https://freeonlinetools24.com/")


@pytest.fixture(scope='session')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture()
def homepage(request):
    baseurl = request.config.getoption("--baseurl")
    return baseurl
