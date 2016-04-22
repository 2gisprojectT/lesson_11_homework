from Base_component import BaseComponent
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Info_about_flight(BaseComponent):

    selectors = {
        'one_direction': 'li.searchFormABWayControlItem:nth-child(3)',
        'two_direction': 'li.searchFormABWayControlItem:nth-child(2)',
        'from': '#from0',
        'to': '#to0',
        'date0': '/html/body/div[12]/div[2]/table/tbody/tr/td[1]/table/tbody/tr[4]/td[7]/div/div[2]',
        'date1': '/html/body/div[12]/div[2]/table/tbody/tr/td[1]/table/tbody/tr[4]/td[6]/div/div[2]',
        'button_date_back': '//*[@id="date1"]',
        'button_find': '.searchFormABSubmit',
        'error': '.comment > p:nth-child(1)'
    }

    def from_to(self, _from, _to):
        elem = self.driver.find_element_by_css_selector(self.selectors['from'])
        elem.send_keys(_from)
        elem = self.driver.find_element_by_css_selector(self.selectors['to'])
        elem.send_keys(_to)

    def date_to(self):
        elem = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, self.selectors['date0'])))
        elem.click()

    def date_back(self):
        elem = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, self.selectors['button_date_back'])))
        elem.click()
        elem = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, self.selectors['date1'])))
        elem.click()

    def two_directions(self):
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.selectors['two_direction']))).click()

    def one_direction(self):
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.selectors['one_direction']))).click()

    def button_find(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, self.selectors['button_find']))).click()

    @property
    def error(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.selectors['error']))).text