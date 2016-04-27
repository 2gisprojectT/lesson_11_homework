from Head import Head
class Filling_email_form(Head):

    def enter_email(self, text):
        self.email = self.driver.find_element_by_name("Email")
        self.email.send_keys(text)
        self.email.submit()

    def get_error(self):
        return self.driver.find_element_by_css_selector(".has-error .error-msg").text
