from Base_component import BaseComponent
from selenium.webdriver.common.keys import Keys

class Passenger(BaseComponent):

    selectors = {
        'email': '#input_avia_book_email',
        'lastname': '#input_lastName0',
        'firstname': '#input_firstName0',
        'passport': '#input_passNumber0',
        'error': '.comment > p:nth-child(1)',
        'go_on': '//*[@id="popup_passengerSelect"]/form/div[2]/div[9]/button'
    }

    def set_passenger_inf(self, email, lastname, firstName, passport):
        elem = self.driver.find_element_by_css_selector(self.selectors['email'])
        elem.send_keys(email)
        elem = self.driver.find_element_by_css_selector(self.selectors['lastname'])
        elem.send_keys(lastname)
        elem = self.driver.find_element_by_css_selector(self.selectors['firstname'])
        elem.send_keys(firstName)
        elem.send_keys(Keys.TAB, Keys.NUMPAD0, Keys.NUMPAD4, Keys.NUMPAD0, Keys.NUMPAD4, Keys.NUMPAD2, Keys.NUMPAD0,
                       Keys.NUMPAD1, Keys.NUMPAD6)
        elem = self.driver.find_element_by_css_selector(self.selectors['passport'])
        elem.send_keys(passport)

    def next_step(self):
        self.driver.find_element_by_xpath(self.selectors['go_on']).click()

    @property
    def error(self):
        return self.driver.find_element_by_css_selector(self.selectors['error']).text