class Page:
    def __init__(self, driver):
        self.driver = driver
        self._elementClassName = None
        self._elementName = None
        self._button = None

    @property
    def element_class_name(self):
        from element_by_class_name import ByClassName
        if self._elementClassName == None:
            self._elementClassName = ByClassName(self.driver)
        return self._elementClassName

    @property
    def element_name(self):
        from element_by_name import ByName
        if self._elementName == None:
            self._elementName = ByName(self.driver)
        return self._elementName

    @property
    def button(self):
        from element_button import Button
        if self._button == None:
            self._button = Button(self.driver)
        return self._button

    def open(self, url):
        self.driver.get(url)