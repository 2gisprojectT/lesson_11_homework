from base_component import BaseComponent


class SearchResult(BaseComponent):
    selectors = {
        'self': '.searchResults__list',
        'first_result': 'article#module-1-12-1-1-1-3 a.miniCard__headerTitleLink'
    }

    def first_result(self):
        self.driver.find_element_by_css_selector(self.selectors['first_result']).click()
