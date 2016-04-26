from base_component import BaseComponent


class PassengerInfo(BaseComponent):
    id = {
        'button_add_passenger': 'button_addPassenger',
        'last_name': 'input_lastName0',
        'first_name': 'input_firstName0',
        'birth_date': 'input_birthDate0',
        'pass_num': 'input_passNumber0',
        'pass_exp_date': 'input_passExpDate0',
        'save_passenger': 'button_savePassengers',
    }

    def add_passenger(self, passenger_info):
        self.driver.find_element_by_id(self.id['button_add_passenger']).click()
        self.driver.find_element_by_id(self.id['last_name']).send_keys(passenger_info[0])
        self.driver.find_element_by_id(self.id['first_name']).send_keys(passenger_info[1])
        self.driver.find_element_by_id(self.id['birth_date']).send_keys(passenger_info[2])
        self.driver.find_element_by_id(self.id['pass_num']).send_keys(passenger_info[3])
        self.driver.find_element_by_id(self.id['pass_exp_date']).send_keys(passenger_info[4])
        self.driver.find_element_by_id(self.id['save_passenger']).click()
        self.driver.refresh()

    def get_passenger_info(self):
        last_name = self.driver.find_element_by_id(self.id['last_name']).get_attribute("value")
        first_name = self.driver.find_element_by_id(self.id['first_name']).get_attribute("value")
        birth_date = self.driver.find_element_by_id(self.id['birth_date']).get_attribute("value")
        pass_number = self.driver.find_element_by_id(self.id['pass_num']).get_attribute("value")
        pass_exp_date = self.driver.find_element_by_id(self.id['pass_exp_date']).get_attribute("value")
        passenger_info = (last_name, first_name, birth_date, pass_number, pass_exp_date)
        return passenger_info
