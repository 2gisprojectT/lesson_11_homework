from base_component import BaseComponent


class FrameResultSearchPassage(BaseComponent):

    selectors = {
        'self': '.dataViewer',
        'public_transport_result_list': '.routeResults',
        'car_result_list': ".autoResults",
        'no_results_list': ".noResults__routeType"
    }

    def get_public_transport_text(self):
        return self.driver.find_element_by_css_selector(self.selectors['public_transport_result_list']).text

    def check_no_results_is_displayed(self):
        return self.driver.find_element_by_css_selector(self.selectors['no_results_list']).is_displayed

    def get_auto_transport_text(self):
        return self.driver.find_element_by_css_selector(self.selectors['car_result_list']).text
