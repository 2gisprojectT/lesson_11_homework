class RegisterGoogleEmailPage():
    def __init__(self, driver):

        self.driver = driver
        self._google_email_form = None

    @property
    def google_email_form(self):
        from google_email_form import GoogleEmailForm
        if self._google_email_form is None:
            self._google_email_form = GoogleEmailForm(self.driver)
        return self._google_email_form