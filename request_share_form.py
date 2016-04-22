from base_component import BaseComponent


class RequestShareForm(BaseComponent):
    selectors = {
        'self': 'db-modal-box',
        'link': 'drop-link-field',
        'done': 'button-primary'
    }

    def get_link(self):
        return self.driver.find_element_by_id(self.selectors['link']).get_attribute("value")

    def done(self):
        self.driver.find_element_by_class_name(self.selectors['done']).click()


