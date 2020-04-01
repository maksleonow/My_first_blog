from selenium import webdriver
import pytest

@pytest.fixture(scope='function')
def browser(request):
    print("\nstart browser")
    browser = webdriver.Chrome()
    yield browser
    print("\nstop browser")
    browser.quit()