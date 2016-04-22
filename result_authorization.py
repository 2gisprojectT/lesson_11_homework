from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base_component import BaseComponent


class AuthResult(BaseComponent):
    class_name = {
        'name_profile': 'myprofile',
        'error_message': 'Error'
    }

    def user_name(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.class_name['name_profile'])))
        return self.driver.find_element_by_class_name(self.class_name['name_profile']).text

    def message_incorret_login(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.class_name['error_message'])))
        return self.driver.find_element_by_class_name(self.class_name['error_message']).text
