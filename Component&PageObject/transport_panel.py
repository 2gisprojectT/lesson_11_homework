from base_component import BaseComponent


class TransportPanel(BaseComponent):

    selectors = {
        'self': ".searchBar__transport",
        'car_button': ".searchBar__transportCar",
        'public_button': ".searchBar__transportBus",
        'subway_button': ".searchBar__transportSubway"
    }

    def car_button_click(self):
        self.driver.find_element_by_css_selector(self.selectors['car_button']).click()

    def public_button_click(self):
        self.driver.find_element_by_css_selector(self.selectors['public_button']).click()

    def subway_button_click(self):
        self.driver.find_element_by_css_selector(self.selectors['subway_button']).click()