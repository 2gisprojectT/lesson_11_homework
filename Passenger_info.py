from Base_component import BaseComponent
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Passenger(BaseComponent):

    selector = {
        'email': '#input_avia_book_email',
        'lastname': '#input_lastName0',
        'firstname': '#input_firstName0',
        'passport': '#input_passNumber0',
        'error': '.comment > p:nth-child(1)'
    }

    def passenger_inf(self, email, lastname, firstName, passport):
        elem = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.selector['email'])))
        elem.send_keys(email)
        elem = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.selector['lastname'])))
        elem.send_keys(lastname)
        elem = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.selector['firstname'])))
        elem.send_keys(firstName)
        elem.send_keys(Keys.TAB, Keys.NUMPAD0, Keys.NUMPAD4, Keys.NUMPAD0, Keys.NUMPAD4, Keys.NUMPAD2, Keys.NUMPAD0,
                       Keys.NUMPAD1, Keys.NUMPAD6)
        elem = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.selector['passport'])))
        elem.send_keys(passport)
        elem.send_keys(Keys.TAB, Keys.ENTER)

    @property
    def error(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.selector['error']))).text