__author__ = 'olga.ostapenko'


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, email):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//div[@class='btn-box']//div[.='Let’s get started!']").click()
        wd.find_element_by_link_text("Log in").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_xpath("//div[@class='form-login']//button[.='Request token']").click()
