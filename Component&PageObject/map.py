from base_component import BaseComponent
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Map(BaseComponent):
    selectors = {
        'self': 'map',
        'route_pin': ".map__markerRouteSearchPin"
    }

    def search_passage_by_clicking_on_objects(self, obj1, obj2):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, obj1)))
        self.driver.find_element_by_xpath(obj1).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.selectors['route_pin'])))
        self.driver.find_element_by_xpath(obj2).click()
