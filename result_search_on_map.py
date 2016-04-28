from base_component import BaseComponent


class ResultSearchOnMap(BaseComponent):

    selectors = {
        'self': "map",
        'search_path': "path[class='routeSearchGeometry leaflet-interactive']"
    }

    def check_passage_is_displayed(self):
        return self.driver.find_element_by_css_selector(self.selectors['search_path']).is_displayed()
