class RegisterGooglePasswordPage():
    def __init__(self, driver):

        self.driver = driver
        self._google_password_form = None

    @property
    def google_password_form(self):
        from google_password_form import GooglePasswordForm
        if self._google_password_form is None:
            self._google_password_form = GooglePasswordForm(self.driver)
        return self._google_password_form