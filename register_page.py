class RegisterPage():
    def __init__(self, driver):

        self.driver = driver
        self._registration_form = None
        self._password_field = None
        self._captcha_form = None

    @property
    def registration_form(self):
        from registration_form import RegistrationForm
        if self._registration_form is None:
            self._registration_form = RegistrationForm(self.driver)
        return self._registration_form

    @property
    def password_field(self):
        from password_field import PasswordField
        if self._password_field is None:
            self._password_field = PasswordField(self.driver)
        return self._password_field

    @property
    def captcha_form(self):
        from captcha_form import CaptchaForm
        if self._captcha_form is None:
            self._captcha_form = CaptchaForm(self.driver)
        return self._captcha_form

    def open(self, url):
        self.driver.get(url)
