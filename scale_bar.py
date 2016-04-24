from page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base_component import BaseComponent


class ScaleBar(BaseComponent):
    selectors = {
        'self': '._zoom',
        'increase': '._zoom__inButton'
    }

    __place_coordinates_with_zoom = {
        'Центральный округ': {1: [950, 300]}
    }

    def increase(self, count):
        while count > 0:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'map')))
            self.driver.find_element_by_css_selector(self.selectors['increase']).click()
            count -= 1
            Page.scale += 1
