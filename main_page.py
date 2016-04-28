from search_bar import SearchBar


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar_ = None

    @property
    def search_bar(self):
        if self.search_bar_ is None:
            self.search_bar_ = SearchBar(self.driver)
        return self.search_bar_

    @property
    def page_source(self):
        return self.driver.page_source

    def open(self, url):
        self.driver.get(url)
