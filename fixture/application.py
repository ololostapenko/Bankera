__author__ = 'olga.ostapenko'

from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://demo-test-stage.exmarkets.com/")

    def destroy(self):
        self.wd.quit()