from base_component import BaseComponent


class SearchBar(BaseComponent):

    selectors = {
        'self': ".searchBar",
        'way_button': "searchBar__buttons"
    }

    def select_passage(self):
        self.driver.find_element_by_class_name(self.selectors['way_button']).click()