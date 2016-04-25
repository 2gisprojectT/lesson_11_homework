from BaseComponent import BaseComponent


class DropsManagementGrid(BaseComponent):
    selectors = {
        "newRequestBtn": "drops-grid-create-new-item",
        "requests": "actions__link"
    }

    def create_request(self):
        self.driver.find_element_by_class_name(self.selectors["newRequestBtn"]).click()

    def show_request(self, i):
        self.driver.find_elements_by_class_name(self.selectors["requests"])[i].click()

