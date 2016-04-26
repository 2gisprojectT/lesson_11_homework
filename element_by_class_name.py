from base_component import BaseComponent
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.common.by import By


class ByClassName(BaseComponent):
    def fill(self, element_class_name, query, key1=None, key2=None):
        self.driver.find_element_by_class_name(element_class_name).send_keys(query, key1, key2)

    def wait_text(self, element_class_name, text):
        return WW(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, element_class_name), text))