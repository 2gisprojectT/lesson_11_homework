from base_component import BaseComponent


class SearchButton(BaseComponent):

    selectors = {
        'self': ".searchBar__buttons",
        'way_button': "searchBar__buttons"
    }

    def way_button(self):
        self.driver.find_element_by_class_name(self.selectors['way_button']).click()