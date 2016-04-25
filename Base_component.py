

class BaseComponent(object):
    def __init__(self, driver, wait, element=None):
        """
        :type driver: WebDriver
        :type element: WebElement
        """
        self.driver = driver
        self.wait = wait
        self.element = element
