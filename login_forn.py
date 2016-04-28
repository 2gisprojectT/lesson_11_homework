from base_component import BaseComponent


class LoginForm(BaseComponent):
    selectors = {
        "email": "Email",
        "password": "Passwd",
        "next": "next",
        "sign_in": "signIn"
    }

    def login(self, email, passwd):
        self.driver.find_element_by_id(self.selectors["email"]).send_keys(email)
        self.driver.find_element_by_id(self.selectors["next"]).click()
        self.driver.find_element_by_id(self.selectors["password"]).send_keys(passwd)
        self.driver.find_element_by_id(self.selectors["sign_in"]).click()
