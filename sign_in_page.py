class SignInPage():

    def __init__(self, driver):
        self.driver = driver
        self._sign_in_form = None

    @property
    def sign_in_form(self):
        from sign_in_form import SignInForm
        if self._sign_in_form is None:
            self._sign_in_form = SignInForm(self.driver)
        return self._sign_in_form

    def open(self, url):
        self.driver.get(url)