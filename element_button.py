from base_component import BaseComponent


class Button(BaseComponent):
    def click(self, element_class_name):
        self.driver.find_element_by_class_name(element_class_name).click()