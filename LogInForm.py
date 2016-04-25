from selenium.webdriver.common.keys import Keys

from BaseComponent import BaseComponent


class LogInForm(BaseComponent):
    selectors = {
        "email": ".//input[@name='login_email']",
        "password": ".//input[@name='login_password']"
    }

    def login(self, email, passwd):
        self.driver.find_element_by_xpath(self.selectors["email"]).send_keys(email)
        passwd_field = self.driver.find_element_by_xpath(self.selectors["password"]).send_keys(passwd+Keys.RETURN)