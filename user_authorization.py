from base_component import BaseComponent


class UserAuthorization(BaseComponent):
    id = {
        'input_email': 'input_auth_email',
        'input_pass': 'input_auth_pas',
        'twitter_email': 'username_or_email',
        'twitter_pass': 'password',
        'twitter_submit': 'allow'
    }
    selector = {
        'twitter_button': '.sLinks_inside > ul:nth-child(2) > li:nth-child(2)'
    }
    class_name = {
        'user_profile': 'knownUser',
        'error_info': 'Error',
        'submit': 'pos_but',
        'login': 'reg'
    }

    def authorization(self, email, password):
        self.driver.find_element_by_id(self.id['input_email']).send_keys(email)
        self.driver.find_element_by_id(self.id['input_pass']).send_keys(password)
        self.driver.find_element_by_class_name(self.class_name['submit']).click()

    def twitter_authorization(self, email, password):
        self.driver.find_element_by_css_selector(self.selector['twitter_button']).click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_id(self.id['twitter_email']).send_keys(email)
        self.driver.find_element_by_id(self.id['twitter_pass']).send_keys(password)
        self.driver.find_element_by_id(self.id['twitter_submit']).submit()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.driver.find_element_by_class_name(self.class_name['user_profile']).click()

    def get_error_auth(self):
        return self.driver.find_element_by_class_name(self.class_name['error_info']).text

    def get_auth_info(self):
        return self.driver.find_element_by_class_name(self.class_name['login']).text

