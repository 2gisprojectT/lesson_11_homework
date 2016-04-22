class UserAuthPage:
    def __init__(self, driver):
        self.driver = driver
        self._user_authorization = None

    @property
    def user_auth(self):
        from user_authorization import UserAuthorization
        if self._user_authorization is None:
            self._user_authorization = UserAuthorization(self.driver)
        return self._user_authorization
