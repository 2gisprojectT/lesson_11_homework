from base_component import BaseComponent
from selenium.webdriver.common.keys import Keys


class SendForm(BaseComponent):
    selectors = {
        "dest": "to",
        "theme": "subjectbox",
        "body": "LW-avf"
    }

    def fill_n_send(self, dest, theme, body):
        self.driver.find_element_by_name(self.selectors["dest"]).send_keys(dest, Keys.TAB)
        self.driver.find_element_by_name(self.selectors["theme"]).send_keys(theme, Keys.TAB)
        self.driver.find_element_by_class_name(self.selectors["body"]).send_keys(body, Keys.TAB, Keys.ENTER)

    def fill_not_all(self):
        self.driver.find_element_by_class_name(self.selectors["body"]).send_keys("just one moment...")