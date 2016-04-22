from base_component import BaseComponent


class SearchResultList(BaseComponent):

    selectors = {
        'result_list': '.routeResults',
        'car_result_list': ".autoResults",
        'no_results_list': ".noResults__routeType"
    }

    def public_transport_result_list_text(self):
        return self.driver.find_element_by_css_selector(self.selectors['result_list']).text

    def no_results_list_displayed(self):
        return self.driver.find_element_by_css_selector(self.selectors['no_results_list']).is_displayed

    def car_result_list_text(self):
        return self.driver.find_element_by_css_selector(self.selectors['car_result_list']).text
