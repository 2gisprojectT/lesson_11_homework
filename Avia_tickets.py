from Base_component import BaseComponent


class InfoAboutFlight(BaseComponent):

    selectors = {
        'one_direction': 'li.searchFormABWayControlItem:nth-child(3)',
        'two_direction': 'li.searchFormABWayControlItem:nth-child(2)',
        'from': '#from0',
        'to': '#to0',
        'date0': '/html/body/div[12]/div[2]/table/tbody/tr/td[1]/table/tbody/tr[5]/td[6]/div/div[2]',
        'date1': '/html/body/div[12]/div[2]/table/tbody/tr/td[1]/table/tbody/tr[5]/td[5]/div/div[2]',
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
        self.driver.find_element_by_xpath(self.selectors['date0']).click()

    def date_back(self):
        self.driver.find_element_by_xpath(self.selectors['button_date_back']).click()
        self.driver.find_element_by_xpath(self.selectors['date1']).click()

    def select_two_directions(self):
        self.driver.find_element_by_css_selector(self.selectors['two_direction']).click()

    def select_one_direction(self):
        self.driver.find_element_by_css_selector(self.selectors['one_direction']).click()

    def button_find(self):
        self.driver.find_element_by_css_selector(self.selectors['button_find']).click()

    @property
    def error(self):
        return self.driver.find_element_by_css_selector(self.selectors['error']).text