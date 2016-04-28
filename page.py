class Page:
    def __init__(self, driver):
        self.driver = driver
        self._send = None
        self._authorization = None
        self._message = None

    @property
    def send_form(self):
        from send_form import SendForm
        if self._send == None:
            self._send = SendForm(self.driver)
        return self._send

    @property
    def authorization(self):
        from authorization_form import Authorization
        if self._authorization == None:
            self._authorization = Authorization(self.driver)
        return self._authorization

    @property
    def message_sending(self):
        from message_sending import Message
        if self._message == None:
            self._message = Message(self.driver)
        return self._message

    def open(self, url):
        self.driver.get(url)