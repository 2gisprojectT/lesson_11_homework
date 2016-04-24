class BaseComponent(object):
    def __init__(self, driver, actions=None, element=None):
        """
        :type driver: WebDriver
        :type element: WebElement
        :type actions: ActionChains
        """
        self.driver = driver
        self.actions = actions
        self.element = element
