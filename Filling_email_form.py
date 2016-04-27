from head import Head
class FillingEmailForm(Head):

    def enter_email(self, email_input):
        email = self.driver.find_element_by_name("Email")
        email.send_keys(email_input)
        email.submit()

    def get_error(self):
        return self.driver.find_element_by_css_selector(".has-error .error-msg").text
