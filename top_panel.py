from base_component import BaseComponent


class TopPanel(BaseComponent):
    class_name = {'login': "enter"}

    def click_login(self):
        self.driver.find_element_by_class_name(self.class_name['login']).click()
