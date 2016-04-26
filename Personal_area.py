from Base_component import BaseComponent
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class PersonalArea(BaseComponent):

    selectors = {
        'enter': '.enter',
        'twit': '//*[@id="SocialAuth"]/div[2]/ul/li[2]/a',
        'log': '#username_or_email',
        'pass': '#password',
        'ok': '#allow',
        'myprof': 'myprofile',
        'reg_email': '#input_reg_email',
        'reg_pass': '#input_reg_pas',
        'repeat_pass': '#input_confirmreg_pas',
        'reg_form': '//*[@id="SocialRegAuth"]'
    }

    def personal_area_click(self):
        self.driver.find_element_by_css_selector(self.selectors['enter']).click()

    def twitt_logo_click(self):
        self.driver.find_element_by_xpath(self.selectors['twit']).click()

    def input_inf(self, name, password):
        self.driver.switch_to_window(self.driver.window_handles[1])
        elem = self.driver.find_element_by_css_selector(self.selectors['log'])
        elem.send_keys(name)
        elem = self.driver.find_element_by_css_selector(self.selectors['pass'])
        elem.send_keys(password)
        self.driver.find_element_by_css_selector(self.selectors['ok']).click()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def check_name(self, name):
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, self.selectors['myprof']), name))

    def input_reg_inf(self, name, password1, password2):
        elem = self.driver.find_element_by_css_selector(self.selectors['reg_email'])
        elem.send_keys(name)
        elem = self.driver.find_element_by_css_selector(self.selectors['reg_pass'])
        elem.send_keys(password1)
        elem = self.driver.find_element_by_css_selector(self.selectors['repeat_pass'])
        elem.send_keys(password2)
        elem.send_keys(Keys.TAB, Keys.ENTER)

    @property
    def active_form(self):
        return self.driver.find_element_by_xpath(self.selectors['reg_form']).is_displayed()