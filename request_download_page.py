class RequestDownloadPage:
    def __init__(self, driver):
        self.driver = driver
        self._request_download_panel = None
        self._request_download_header = None

    @property
    def request_download_panel(self):
        from request_download_panel import RequestDownloadPanel
        if self._request_download_panel is None:
            self._request_download_panel = RequestDownloadPanel(self.driver, self.driver.find_element_by_class_name(RequestDownloadPanel.selectors['self']))
        return self._request_download_panel

    @property
    def request_download_header(self):
        from request_download_header import RequestDownloadHeader
        if self._request_download_header is None:
            self._request_download_header = RequestDownloadHeader(self.driver, self.driver.find_element_by_class_name(RequestDownloadHeader.selectors['self']))
        return self._request_download_header

    def open(self, url):
        self.driver.get(url)

