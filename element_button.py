from base_component import BaseComponent


class Button(BaseComponent):
    def click(self):
        self.driver.find_element_by_class_name("z0").click()
