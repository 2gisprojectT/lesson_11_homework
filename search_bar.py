from base_component import BaseComponent


class SearchBar(BaseComponent):
    selectors = {
        "search_form": "gbqfq",
        "search_button": "gbqfb",
        "from": "/html/body/div/div/div/div/span/input",
        "size": "//input[@aria-label='Значение размера']",
        "search_param_button": "gbqfab"

    }

    def search(self, search_text):
        self.driver.find_element_by_id(self.selectors["search_form"]).send_keys(search_text)
        self.driver.find_element_by_id(self.selectors["search_button"]).click()

    def add_param_size(self, size):
        self.driver.find_element_by_id(self.selectors["search_param_button"]).click()
        self.driver.find_element_by_xpath(self.selectors["size"]).send_keys(size)

    def add_param_from(self, from_):
        self.driver.find_element_by_id(self.selectors["search_param_button"]).click()
        self.driver.find_element_by_xpath(self.selectors["from"]).send_keys(from_)
