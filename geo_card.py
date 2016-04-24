from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base_component import BaseComponent


class GeoCard(BaseComponent):
    selectors = {
        'self': '.geoCard2',
        'title': '.geoCard2__name',
        'near_stop': 'geoCard2__nearStopLink',
        'address_link': 'geoCard2__addressLink',
        'photos': 'geoCard2__photos'
    }

    @property
    def title(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors['title'])))
        return self.driver.find_element_by_css_selector(self.selectors['title']).text

    def near_stop(self):
        self.driver.find_element_by_css_selector(self.selectors['near_stop']).click()

    @property
    def address_link(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors['title'])))
        return self.driver.find_element_by_css_selector(self.selectors['address_link'])

    def photos(self):
        self.driver.find_element_by_css_selector(self.selectors['photos']).click()
