from base_component import BaseComponent


class RequestDownloadHeader(BaseComponent):
    selectors = {
        'self': 'file_collector__deadlines-pill',
        'deadline': 'c-banner',
    }

    def get_deadline(self):
        header = self.driver.find_element_by_class_name(self.selectors['deadline'])
        return header.text





