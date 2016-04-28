from base_component import BaseComponent
from selenium.webdriver.common.keys import Keys


class Authorization(BaseComponent):
    selectors = {
        "email": "Email",
        "passwd": "Passwd",
    }

    def to_authorize(self, email, passwd):
        self.driver.find_element_by_name(self.selectors["email"]).send_keys(email, Keys.RETURN)
        self.driver.find_element_by_name(self.selectors["passwd"]).send_keys(passwd, Keys.RETURN)