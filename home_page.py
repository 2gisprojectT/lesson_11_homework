class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self._main_panel = None

    @property
    def main_panel(self):
        from main_panel import MainPanel
        if self._main_panel is None:
            self._main_panel = MainPanel(self.driver, self.driver.find_element_by_id(MainPanel.selectors['self']))
        return self._main_panel

    def open(self, url):
        self.driver.get(url)

