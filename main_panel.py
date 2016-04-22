from base_component import BaseComponent


class MainPanel(BaseComponent):
    selectors = {
        'self': 'main-nav',
        'requests': 'drops-nav-item',
    }

    def requests(self):
        self.driver.find_element_by_class_name(self.selectors['requests']).click()


