from base_component import BaseComponent


class RequestDownloadPanel(BaseComponent):
    selectors = {
        'self': 'file-collector__submission-page',
        'title': 'info__title',
    }

    def get_title(self):
        return self.driver.find_element_by_class_name(self.selectors['title']).text






