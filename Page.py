class PageLogin():
    def __init__(self, driver):

        self.driver = driver
        self._form_authorization = None
        self._result_authorization = None
        self._resul_forgot_pass = None

    @property
    def form_auth(self):
        from form_authorization import FormAuthorization

        if self._form_authorization is None:
            self._form_authorization = FormAuthorization(self.driver)
        return self._form_authorization

    @property
    def result_auth(self):
        from result_authorization import AuthResult

        if self._result_authorization is None:
            self._result_authorization = AuthResult(self.driver)
        return self._result_authorization

    @property
    def result_forgot_pass(self):
        from result_forgot_pass import ForgotPassResult

        if self._resul_forgot_pass is None:
            self._resul_forgot_pass = ForgotPassResult(self.driver)
        return self._resul_forgot_pass

    def open(self, url):
        self.driver.get(url)