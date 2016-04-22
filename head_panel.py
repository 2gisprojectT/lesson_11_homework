from base_component import BaseComponent


class HeadPanel(BaseComponent):
    selectors = {
        'self': 'mast-head__container',
        'sign_in_button': 'sign-in',
        'login': ".//input[@name='login_email']",
        'password': ".//input[@name='login_password']",
        'login_button': 'login-button',
    }

    def sign_in(self, login, password):
        self.driver.find_element_by_id(self.selectors['sign_in_button']).click()
        self.driver.find_element_by_xpath(self.selectors['login']).send_keys(login)
        self.driver.find_element_by_xpath(self.selectors['password']).send_keys(password)
        self.driver.find_element_by_class_name(self.selectors['login_button']).click()


