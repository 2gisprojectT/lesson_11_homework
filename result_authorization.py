from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base_component import BaseComponent


class AuthResult(BaseComponent):
    class_name = {
        'name_profile': 'myprofile',
        'error_message': 'Error'
    }

    def get_user_name(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.class_name['name_profile'])))
        return self.driver.find_element_by_class_name(self.class_name['name_profile']).text

    def get_incorrect_login_message(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.class_name['error_message'])))
        return self.driver.find_element_by_class_name(self.class_name['error_message']).text
