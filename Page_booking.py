class Page_booking():
    def __init__(self, driver, wait):

        self.driver = driver
        self.wait = wait
        self.passenger_inf = None
        self.choice_flight = None

    @property
    def inf_about_passenger(self):
        from Passenger_info import Passenger

        if self.passenger_inf is None:
            self.passenger_inf = Passenger(self.driver, self.wait)
        return self.passenger_inf

    @property
    def choose_flight(self):
        from Flight import Flight

        if self.choice_flight is None:
            self.choice_flight = Flight(self.driver, self.wait)
        return self.choice_flight

    def open(self, url):
        self.driver.get(url)