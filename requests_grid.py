from base_component import BaseComponent


class RequestsGrid(BaseComponent):
    selectors = {
        'self': 'drops-management-grid-view',
        'create_request': 'drops-grid-create-new-item',
        'edit_request': 'actions__link',
    }

    def create_request(self):
        self.driver.find_element_by_class_name(self.selectors['create_request']).click()

    def edit_request(self, i):
        self.driver.find_elements_by_class_name(self.selectors['edit_request'])[i * 2].click()

