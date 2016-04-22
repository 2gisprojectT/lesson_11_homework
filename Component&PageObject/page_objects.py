

class PageObjects():
    
    def __init__(self, driver):
        self.driver = driver
        self._search_button = None
        self._search_way_panel = None
        self._result_list = None
        self._no_results_list = None
        self._search_result_map = None
        self._car_results_list = None
        self._map = None
        self._zoom_panel = None
        self._transport_panel = None

    @property
    def search_button(self):
        from search_button import SearchButton
        if self._search_button is None:
            self._search_button = SearchButton(self.driver, self.driver.find_element_by_css_selector(SearchButton.selectors['self']))
        return self._search_button

    @property
    def search_way_panel(self):
        from search_way_panel import SearchWayPanel
        if self._search_way_panel is None:
            self._search_way_panel = SearchWayPanel(self.driver, self.driver.find_element_by_css_selector(SearchWayPanel.selectors['self']))
        return self._search_way_panel

    @property
    def map(self):
        from map import SearchMap
        if self._map is None:
            self._map = SearchMap(self.driver, self.driver.find_element_by_class_name(SearchMap.selectors['self']))
        return self._map

    @property
    def zoom_panel(self):
        from zoom_panel import ZoomPanel
        if self._zoom_panel is None:
            self._zoom_panel = ZoomPanel(self.driver, self.driver.find_element_by_class_name(ZoomPanel.selectors['self']))
        return self._zoom_panel

    @property
    def transport_panel(self):
        from transport_panel import TransportPanel
        if self._transport_panel is None:
            self._transport_panel = TransportPanel(self.driver, self.driver.find_element_by_css_selector(TransportPanel.selectors['self']))
        return self._transport_panel

    @property
    def result_list(self):
        from search_result_list import SearchResultList
        if self._result_list is None:
            self._result_list = SearchResultList(self.driver, self.driver.find_element_by_css_selector(SearchResultList.selectors['result_list']))
        return self._result_list

    @property
    def car_result_list(self):
        from search_result_list import SearchResultList
        if self._car_results_list is None:
            self._car_results_list = SearchResultList(self.driver, self.driver.find_element_by_css_selector(SearchResultList.selectors['car_result_list']))
        return self._car_results_list

    @property
    def no_results_list(self):
        from search_result_list import SearchResultList
        if self._no_results_list is None:
            self._no_results_list = SearchResultList(self.driver, self.driver.find_element_by_css_selector(SearchResultList.selectors['no_results_list']))
        return self._no_results_list

    @property
    def search_result_map(self):
        from search_result_map import SearchResultMap
        if self._search_result_map is None:
            self._search_result_map = SearchResultMap(self.driver, self.driver.find_element_by_class_name(SearchResultMap.selectors['self']))
        return self._search_result_map

    def open(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()

