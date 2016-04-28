from base_component import BaseComponent
from selenium.webdriver.common.keys import Keys


class SendForm(BaseComponent):
    selectors = {
        "open": "z0",
        "dest": "to",
        "theme": "subjectbox",
        "body": "LW-avf"
    }

    def open_form(self):
        self.driver.find_element_by_class_name(self.selectors["open"]).click()

    def send_email(self, dest, theme, body):
        self.driver.find_element_by_name(self.selectors["dest"]).send_keys(dest, Keys.TAB)
        self.driver.find_element_by_name(self.selectors["theme"]).send_keys(theme, Keys.TAB)
        self.fill_body_field(body, Keys.TAB, Keys.ENTER)

    def fill_body_field(self, text, key1="", key2=""):
        self.driver.find_element_by_class_name(self.selectors["body"]).send_keys(text, key1, key2)