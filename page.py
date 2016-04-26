class Page:
    def __init__(self, driver, actions):

        self.driver = driver
        self.actions = actions
        self._search_bar = None
        self._search_result = None
        self._scale_bar = None
        self._map = None
        self._geo_card = None
        self._firm_card = None
        self._metro_card = None
        self._gallery_card = None

    @property
    def map(self):
        from map import Map

        if self._map is None:
            self._map = Map(self.driver, self.actions, self.driver.find_element_by_css_selector(Map.selectors['self']))
        return self._map

    @property
    def geo_card(self):
        from geo_card import GeoCard

        if self._geo_card is None:
            self._geo_card = GeoCard(self.driver, self.actions,
                                     self.driver.find_element_by_css_selector(GeoCard.selectors['self']))
        return self._geo_card

    @property
    def firm_card(self):
        from firm_card import FirmCard

        if self._firm_card is None:
            self._firm_card = FirmCard(self.driver, self.actions,
                                       self.driver.find_element_by_css_selector(FirmCard.selectors['self']))
        return self._firm_card

    @property
    def metro_card(self):
        from metro_card import MetroCard

        if self._metro_card is None:
            self._metro_card = MetroCard(self.driver, self.actions,
                                         self.driver.find_element_by_css_selector(MetroCard.selectors['self']))
        return self._metro_card

    @property
    def gallery_card(self):
        from gallery_card import GalleryCard

        if self._gallery_card is None:
            self._gallery_card = GalleryCard(self.driver, self.actions,
                                             self.driver.find_element_by_css_selector(GalleryCard.selectors['self']))
        return self._gallery_card

    @property
    def scale_bar(self):
        from scale_bar import ScaleBar

        if self._scale_bar is None:
            self._scale_bar = ScaleBar(self.driver, self.actions,
                                       self.driver.find_element_by_css_selector(ScaleBar.selectors['self']))
        return self._scale_bar

    @property
    def search_bar(self):
        from search_bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver, self.actions,
                                         self.driver.find_element_by_css_selector(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def search_result(self):
        from search_result import SearchResult

        if self._search_result is None:
            self._search_result = SearchResult(self.driver, self.actions,
                                               self.driver.find_element_by_css_selector(
                                                   SearchResult.selectors['self']))
        return self._search_result

    def open(self, url):
        self.driver.get(url)
