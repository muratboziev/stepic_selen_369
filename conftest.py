import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    #user_language = request.config.getoption("language")
    user_language = 'fr'

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    # if browser_name == "chrome":
    #     browser = webdriver.Chrome()
    # elif browser_name == "firefox":
    #     browser = webdriver.Firefox()
    # else:
    #     raise pytest.UsageError("--browser_name should be chrome or firefox")
    # yield browser

    browser.quit()