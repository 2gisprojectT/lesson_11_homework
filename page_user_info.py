class UserInfoPage:
    def __init__(self, driver):
        self.driver = driver
        self._user_info = None

    @property
    def user_info(self):
        from user_info import UserInfo
        if self._user_info is None:
            self._user_info = UserInfo(self.driver)
        return self._user_info
