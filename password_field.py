from base_component import BaseComponent

class PasswordField(BaseComponent):

        selectors = {
            'password': ".password-input[name=password]",
            'protection_meter' : "password-input-meter",
            'hint_message' : "password-bubble-title"
        }

        def input_password(self, password):
            self.driver.find_element_by_css_selector(self.selectors['password']).send_keys(password)
            self.driver.find_element_by_css_selector(self.selectors['password']).submit()

        def get_hint(self):
            self.driver.find_element_by_class_name(self.selectors['protection_meter']).click()
            return self.driver.find_element_by_class_name(self.selectors['hint_message']).text