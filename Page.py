class PageLogin():
    def __init__(self, driver):

        self.driver = driver
        self._form_authorization = None

    @property
    def form_auth(self):
        from form_authorization import FormAuthorization

        if self._form_authorization is None:
            self._form_authorization = FormAuthorization(self.driver)
        return self._form_authorization

    def open(self, url):
        self.driver.get(url)