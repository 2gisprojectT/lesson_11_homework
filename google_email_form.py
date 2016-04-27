from base_component import BaseComponent

class GoogleEmailForm(BaseComponent):

        selectors = {
            'email': "//input[contains(@id,'Email')]"
        }

        def input_email(self, name):
            self.driver.find_element_by_xpath(self.selectors['email']).send_keys(name)
            self.driver.find_element_by_xpath(self.selectors['email']).submit()