from filling_email_form import FillingEmailForm
from filling_pass_form import FillingPassForm


class Page:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    @property
    def email_form(self):
        login_form = FillingEmailForm(self.driver)
        return login_form

    @property
    def passwd_form(self):
        passwd_form = FillingPassForm(self.driver)
        return passwd_form
