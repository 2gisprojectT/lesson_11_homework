class Page():
    #def __init__(self, driver, wait):
    #def __init__(self, driver):
    def __init__(self, driver):

        self.driver = driver
        self.info_about_flight = None
        self.autorization = None

    @property
    def inf_about_flight(self):
        from Avia_tickets import InfoAboutFlight

        if self.info_about_flight is None:
            self.info_about_flight = InfoAboutFlight(self.driver)
        return self.info_about_flight

    @property
    def autorize(self):
        from Personal_area import PersonalArea

        if self.autorization is None:
            self.autorization = PersonalArea(self.driver)
        return self.autorization

    def open(self, url):
        self.driver.get(url)