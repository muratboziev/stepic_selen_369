from selenium import webdriver

from selenium.webdriver.chrome.options import Options #

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link_pass(): #browser):
    user_language = 'fr' #

    options = Options() #
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language}) #
    browser = webdriver.Chrome(options=options) #

    browser.get(link)
    button = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket1")
    assert button, "No add to cart button found"
