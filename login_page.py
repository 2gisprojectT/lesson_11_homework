from login_form import LoginForm


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_form_ = None

    @property
    def login_form(self):
        if self.login_form_ is None:
            self.login_form_ = LoginForm(self.driver)
        return self.login_form_

    @property
    def page_source(self):
        return self.driver.page_source

    def open(self, url):
        self.driver.get(url)
