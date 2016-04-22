from Base_component import BaseComponent
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Personal_area(BaseComponent):

    selector = {
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

    def personal_area(self):
        self.driver.find_element_by_css_selector(self.selector['enter']).click()

    def twitt_logo(self):
        elem = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, self.selector['twit'])))
        elem.click()

    def input_inf(self, name, password):
        self.driver.switch_to_window(self.driver.window_handles[1])
        elem = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.selector['log'])))
        elem.send_keys(name)
        elem = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.selector['pass'])))
        elem.send_keys(password)
        elem = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, self.selector['ok'])))
        elem.click()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def check_name(self, name):
        self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, self.selector['myprof']), name))

    def input_reg(self, name, password1, password2):
        elem = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.selector['reg_email'])))
        elem.send_keys(name)
        elem = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.selector['reg_pass'])))
        elem.send_keys(password1)
        elem = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.selector['repeat_pass'])))
        elem.send_keys(password2)
        elem.send_keys(Keys.TAB, Keys.ENTER)

    @property
    def active_form(self):
        return self.driver.find_element_by_xpath(self.selector['reg_form']).is_displayed()