import pytest
from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

from pytest_metadata.plugin import metadata_key
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'nopCommerceV1'
    config.stash[metadata_key]['Tester Name'] = "Sourav"
    config.stash[metadata_key]['Test Name'] = 'Tests'

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('Packages',None)