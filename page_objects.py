

class PageObjects():
    
    def __init__(self, driver):
        self.driver = driver
        self._map = None
        self._search_bar = None
        self._search_passage_bar = None
        self._result_search_on_map = None
        self._frame_result_search_passage = None
        self._zoom_panel = None

    @property
    def map(self):
        from map import Map
        if self._map is None:
            self._map = Map(self.driver, self.driver.find_element_by_class_name(Map.selectors['self']))
        return self._map

    @property
    def search_bar(self):
        from search_bar import SearchBar
        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver, self.driver.find_element_by_css_selector(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def search_passage_bar(self):
        from search_passage_bar import SearchPassageBar
        if self._search_passage_bar is None:
            self._search_passage_bar = SearchPassageBar(self.driver, self.driver.find_element_by_css_selector(SearchPassageBar.selectors['self']))
        return self._search_passage_bar

    @property
    def result_search_on_map(self):
        from result_search_on_map import ResultSearchOnMap
        if self._result_search_on_map is None:
            self._result_search_on_map = ResultSearchOnMap(self.driver, self.driver.find_element_by_class_name(ResultSearchOnMap.selectors['self']))
        return self._result_search_on_map

    @property
    def frame_result_search_passage(self):
        from frame_result_search_passage import FrameResultSearchPassage
        if self._frame_result_search_passage is None:
            self._frame_result_search_passage = FrameResultSearchPassage(self.driver, self.driver.find_element_by_css_selector(FrameResultSearchPassage.selectors['self']))
        return self._frame_result_search_passage

    @property
    def zoom_panel(self):
        from zoom_panel import ZoomPanel
        if self._zoom_panel is None:
            self._zoom_panel = ZoomPanel(self.driver, self.driver.find_element_by_class_name(ZoomPanel.selectors['self']))
        return self._zoom_panel

    def open(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()

