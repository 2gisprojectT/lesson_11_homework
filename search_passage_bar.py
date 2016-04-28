from base_component import BaseComponent


class SearchPassageBar(BaseComponent):

    selectors = {
        'self': ".searchBar__formsIn",
        'from_field': "div[class='searchBar__textfield _from'] input[class='suggest__input']",
        'to_field': "div[class='searchBar__textfield _to'] input[class='suggest__input']",
        'search_button': ".searchBar__submit._rs",
        'transport_button_car': ".searchBar__transportCar",
        'transport_button_public': ".searchBar__transportBus",
        'transport_button_subway': ".searchBar__transportSubway"
    }

    def search(self, obj1, obj2):
        self.driver.find_element_by_css_selector(self.selectors['from_field']).send_keys(obj1)
        self.driver.find_element_by_css_selector(self.selectors['to_field']).send_keys(obj2)
        self.driver.find_element_by_css_selector(self.selectors['to_field']).submit()

    def select_car_route(self):
        self.driver.find_element_by_css_selector(self.selectors['transport_button_car']).click()

    def select_public_transport(self):
        self.driver.find_element_by_css_selector(self.selectors['transport_button_public']).click()

    def select_subway(self):
        self.driver.find_element_by_css_selector(self.selectors['transport_button_subway']).click()
