from base_component import BaseComponent
from selenium.webdriver.support.select import Select


class UserInfo(BaseComponent):
    id = {
        'input_email': 'input_auth_email',
        'input_pass': 'input_auth_pas',
        'save_contacts': 'button_saveContacts',
        'new_pass': 'input_newPas',
        'repeat_new_pass': 'input_repeatPas',
        'save_new_pass': 'button_changePassword'
    }

    class_name = {
        'user_profile': 'knownUser',
        'submit': 'pos_but',
        'change_pass': 'change_pas',
        'info_after_change_pass': 'reason'
    }

    element_name = {
        'country': 'country'
    }

    def authorization_and_go_to_profile(self, email, password):
        self.driver.find_element_by_id(self.id['input_email']).send_keys(email)
        self.driver.find_element_by_id(self.id['input_pass']).send_keys(password)
        self.driver.find_element_by_class_name(self.class_name['submit']).click()
        self.driver.find_element_by_class_name(self.class_name['user_profile']).click()

    def change_country(self, country_name):
        country_field = self.driver.find_element_by_name(self.element_name['country'])
        select = Select(country_field)
        select.select_by_value(country_name)
        self.driver.find_element_by_id(self.id['save_contacts']).submit()
        self.driver.refresh()

    def change_password(self, new_password):
        self.driver.find_element_by_class_name(self.class_name['change_pass']).click()
        self.driver.find_element_by_id(self.id['new_pass']).send_keys(new_password)
        self.driver.find_element_by_id(self.id['repeat_new_pass']).send_keys(new_password)
        self.driver.find_element_by_id(self.id['save_new_pass']).submit()

    def get_change_password_info(self):
        return self.driver.find_element_by_class_name(self.class_name['info_after_change_pass']).text

    def get_country_name(self):
        country_name = self.driver.find_element_by_name(self.element_name['country']).get_attribute("value")
        return country_name

    def is_displayed_to_the_user(self):
        return self.driver.find_element_by_class_name(self.class_name['info_after_change_pass']).is_displayed()
