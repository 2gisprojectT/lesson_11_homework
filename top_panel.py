from base_component import BaseComponent
from Page import PageLogin


class TopPanel(BaseComponent):
    class_name = {
        'button_login': 'enter'
    }

    def click_login(self):
        self.driver.find_element_by_class_name(self.class_name['button_login']).click()
