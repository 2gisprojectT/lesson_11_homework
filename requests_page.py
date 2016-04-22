class RequestsPage:
    def __init__(self, driver):
        self.driver = driver
        self._requests_grid = None
        self._request_edit_form = None
        self._request_share_form = None

    @property
    def requests_grid(self):
        from requests_grid import RequestsGrid
        if self._requests_grid is None:
            self._requests_grid = RequestsGrid(self.driver, self.driver.find_element_by_class_name(RequestsGrid.selectors['self']))
        return self._requests_grid

    @property
    def request_edit_form(self):
        from request_edit_form import RequestEditForm
        if self._request_edit_form is None:
            self._request_edit_form = RequestEditForm(self.driver, self.driver.find_element_by_class_name(RequestEditForm.selectors['self']))
        return self._request_edit_form

    @property
    def request_share_form(self):
        from request_share_form import RequestShareForm
        if self._request_share_form is None:
            self._request_share_form = RequestShareForm(self.driver, self.driver.find_element_by_class_name(RequestShareForm.selectors['self']))
        return self._request_share_form

    def open(self, url):
        self.driver.get(url)

