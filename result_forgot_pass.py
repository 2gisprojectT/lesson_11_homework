from base_component import BaseComponent
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ForgotPassResult(BaseComponent):
    selectors = {
        'mes_incorrect_email': '#RemindAuth > div:nth-child(3)'
    }
    class_name = {
        'mes_get_new_pass': 'smallText'
    }

    def message_incorrect_email(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors['mes_incorrect_email'])))
        return self.driver.find_element_by_css_selector(self.selectors['mes_incorrect_email'])

    def message_get_pass(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.class_name['mes_get_new_pass'])))
        return self.driver.find_element_by_class_name(self.class_name['mes_get_new_pass'])
