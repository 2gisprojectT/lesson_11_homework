from Filling_email_form import Filling_email_form

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    @property
    def login_form(self):
        login_form = Filling_email_form(self.driver)
        return login_form
