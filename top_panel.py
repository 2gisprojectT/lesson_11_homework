from base_component import BaseComponent
from Page import PageLogin


class TopPanel(BaseComponent):
    class_name = {
        'button_personal_area': 'enter'
    }

    def click_button_personal_area(self):
        self.driver.find_element_by_class_name(self.class_name['button_personal_area']).click()
