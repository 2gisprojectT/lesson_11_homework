from base_component import BaseComponent
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.common.by import By


class Message(BaseComponent):
    selectors = {
        "error": "Kj-JD-Jz",
        "success": "vh",
        "save": "aWQ"
    }
    def check_error_message(self, text):
        return WW(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, self.selectors["error"]), text))

    def check_success_message(self, text):
        return WW(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, self.selectors["success"]), text))

    def check_save(self, text):
        return WW(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, self.selectors["save"]), text))