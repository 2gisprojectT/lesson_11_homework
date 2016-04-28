class BaseComponent:
    def __init__(self, driver, element=None):
        self.driver = driver
        self.element = element