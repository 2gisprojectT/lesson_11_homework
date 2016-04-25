class Page():
    def __init__(self, driver, wait):

        self.driver = driver
        self.wait = wait
        self.info_about_flight = None
        self.autorization = None

    @property
    def inf_about_flight(self):
        from Avia_tickets import Info_about_flight

        if self.info_about_flight is None:
            self.info_about_flight = Info_about_flight(self.driver, self.wait)
        return self.info_about_flight

    @property
    def autorize(self):
        from Personal_area import Personal_area

        if self.autorization is None:
            self.autorization = Personal_area(self.driver, self.wait)
        return self.autorization

    def open(self, url):
        self.driver.get(url)