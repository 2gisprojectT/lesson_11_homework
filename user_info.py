from base_component import BaseComponent
from selenium.webdriver.support.select import Select


class UserInfo(BaseComponent):
    id = {
        'input_email': 'input_auth_email',
        'input_pass': 'input_auth_pas',
        'button_add_passenger': 'button_addPassenger',
        'last_name': 'input_lastName0',
        'first_name': 'input_firstName0',
        'birth_date': 'input_birthDate0',
        'pass_num': 'input_passNumber0',
        'pass_exp_date': 'input_passExpDate0',
        'save_passenger': 'button_savePassengers',
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

    def add_passenger(self, passenger_info):
        self.driver.find_element_by_id(self.id['button_add_passenger']).click()
        self.driver.find_element_by_id(self.id['last_name']).send_keys(passenger_info[0])
        self.driver.find_element_by_id(self.id['first_name']).send_keys(passenger_info[1])
        self.driver.find_element_by_id(self.id['birth_date']).send_keys(passenger_info[2])
        self.driver.find_element_by_id(self.id['pass_num']).send_keys(passenger_info[3])
        self.driver.find_element_by_id(self.id['pass_exp_date']).send_keys(passenger_info[4])
        self.driver.find_element_by_id(self.id['save_passenger']).click()
        self.driver.refresh()

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

    def get_element(self):
        return self.driver.find_element_by_class_name(self.class_name['info_after_change_pass'])

    def get_passenger_info(self):
        last_name = self.driver.find_element_by_id(self.id['last_name']).get_attribute("value")
        first_name = self.driver.find_element_by_id(self.id['first_name']).get_attribute("value")
        birth_date = self.driver.find_element_by_id(self.id['birth_date']).get_attribute("value")
        pass_number = self.driver.find_element_by_id(self.id['pass_num']).get_attribute("value")
        pass_exp_date = self.driver.find_element_by_id(self.id['pass_exp_date']).get_attribute("value")
        passenger_info = (last_name, first_name, birth_date, pass_number, pass_exp_date)
        return passenger_info
