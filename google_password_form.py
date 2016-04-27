from base_component import BaseComponent

class GooglePasswordForm(BaseComponent):

        selectors = {
            'password': "Passwd"
        }

        def input_password(self, password):
            self.driver.find_element_by_name(self.selectors['password']).send_keys(password)
            self.driver.find_element_by_name(self.selectors['password']).submit()