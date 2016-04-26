from base_component import BaseComponent

class GoogleRequestForm(BaseComponent):

        selectors = {
            'page_header': "gb_b",
            'account_name': "gb_pb"
        }

        def get_account_name(self):
            self.driver.find_element_by_class_name(self.selectors['page_header']).click()
            return self.driver.find_element_by_class_name(self.selectors['account_name']).text