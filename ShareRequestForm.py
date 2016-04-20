from BaseComponent import BaseComponent


class ShareRequestForm(BaseComponent):
    selectors = {
        "done": "dbmodal-button"
    }

    def done(self):
        self.driver.find_element_by_class_name(self.selectors["done"]).click()