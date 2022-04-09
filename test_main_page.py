from .pages.login_page import LoginPage
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_form_on_login_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
