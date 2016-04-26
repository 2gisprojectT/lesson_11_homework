from base_component import BaseComponent

class RegistrationForm(BaseComponent):

        selectors = {
            'name': ".text-input-input[name=fname]",
            'email': ".text-input-input[name=email]",
            'password': ".password-input[name=password]",
            'agree_checkbox': "//input[@name='tos_agree']",
            'error_message': "error-message",
            'sign_in_link': "//a[contains(@href,'/login')]",
            'register_google' : "auth-google"
        }

        def registration(self, name, email, password):
            self.driver.find_element_by_xpath(self.selectors['agree_checkbox']).click()
            self.driver.find_element_by_css_selector(self.selectors['name']).send_keys(name)
            self.driver.find_element_by_css_selector(self.selectors['email']).send_keys(email)
            self.driver.find_element_by_css_selector(self.selectors['password']).send_keys(password)
            self.driver.find_element_by_css_selector(self.selectors['password']).submit()

        def error_registration(self):
            return self.driver.find_element_by_class_name(self.selectors['error_message']).text

        def go_to_sign_in(self):
            self.driver.find_element_by_xpath(self.selectors['sign_in_link']).click()

        def register_google(self):
            self.driver.find_element_by_class_name(self.selectors['register_google']).click()