class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self._head_panel = None

    @property
    def head_panel(self):
        from head_panel import HeadPanel
        if self._head_panel is None:
            self._head_panel = HeadPanel(self.driver, self.driver.find_element_by_class_name(HeadPanel.selectors['self']))
        return self._head_panel

    def open(self, url):
        self.driver.get(url)

