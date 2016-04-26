class RegisterGoogleRequestPage():
    def __init__(self, driver):

        self.driver = driver
        self._google_request_form = None

    @property
    def google_request_form(self):
        from google_request_form import GoogleRequestForm
        if self._google_request_form is None:
            self._google_request_form = GoogleRequestForm(self.driver)
        return self._google_request_form