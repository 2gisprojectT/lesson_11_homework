from LogInForm import LogInForm


class PageLogin:
    def __init__(self, driver):
        self.driver = driver
        self._login_form = None

    @property
    def login_form(self):
        if self._login_form is None:
            self._login_form = LogInForm(self.driver)
        return self._login_form

    def open(self, url):
        self.driver.get(url)
