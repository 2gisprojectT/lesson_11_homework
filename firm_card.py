from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base_component import BaseComponent


class FirmCard(BaseComponent):
    selectors = {
        'self': '.firmCard',
        'title': '.cardHeader__headerNameText'
    }

    @property
    def title(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors['title'])))
        return self.driver.find_element_by_css_selector(self.selectors['title']).text
