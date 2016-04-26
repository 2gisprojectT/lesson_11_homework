class UserInfoPage:
    def __init__(self, driver):
        self.driver = driver
        self._user_info = None
        self._passenger_info = None

    @property
    def user_info(self):
        from user_info import UserInfo
        if self._user_info is None:
            self._user_info = UserInfo(self.driver)
        return self._user_info

    @property
    def passenger_info(self):
        from passenger_info import PassengerInfo
        if self._passenger_info is None:
            self._passenger_info = PassengerInfo(self.driver)
        return self._passenger_info
