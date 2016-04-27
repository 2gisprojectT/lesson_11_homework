from base_component import BaseComponent
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ZoomPanel(BaseComponent):

    selectors = {
        'self': 'zoom',
        'zoom_button': "div[class='zoom__button _type_in']"
    }

    def click_plus(self, value):
        zoom_button = self.driver.find_element_by_css_selector(self.selectors['zoom_button'])
        while value > 0:
            WebDriverWait(self.driver, value).until(EC.element_to_be_clickable((By.CLASS_NAME, 'map')))
            zoom_button.click()
            value -= 1