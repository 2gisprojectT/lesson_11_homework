class PageBooking():
    def __init__(self, driver):

        self.driver = driver
        self.passenger_inf = None
        self.flight = None

    @property
    def inf_about_passenger(self):
        from Passenger_info import Passenger

        if self.passenger_inf is None:
            self.passenger_inf = Passenger(self.driver)
        return self.passenger_inf

    @property
    def selected_flight(self):
        from Flight import Flight

        if self.flight is None:
            self.flight = Flight(self.driver)
        return self.flight

    def open(self, url):
        self.driver.get(url)