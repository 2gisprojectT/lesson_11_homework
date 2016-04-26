from base_component import BaseComponent

class SignInForm(BaseComponent):

    selectors = {
        'create_account': "login-register-switch-link",
        'register_header' : "login-register-header"
    }

    def switch_to_sign_up(self):
        self.driver.find_element_by_class_name(self.selectors['create_account']).click()

    def get_header_text(self):
        return self.driver.find_element_by_class_name(self.selectors['register_header']).text