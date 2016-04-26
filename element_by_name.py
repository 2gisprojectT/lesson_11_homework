from base_component import BaseComponent
from selenium.webdriver.common.keys import Keys


class ByName(BaseComponent):
    def fill(self, element_name, query):
        self.driver.find_element_by_name(element_name).send_keys(query, Keys.RETURN)