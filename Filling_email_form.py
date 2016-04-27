from head import Head
from selenium.webdriver.support.ui import WebDriverWait

class FillingEmailForm(Head):
    def enter_email(self, email_input):
        self.elem = self.driver.find_element_by_name("Email")
        self.elem.send_keys(email_input)
        self.elem.submit()

    def get_error(self):
        return self.driver.find_element_by_css_selector(".has-error .error-msg").text

    def __infinity_email_loop(self):
        captcha = self.driver.find_element_by_id("captcha-img")
        while (True):
            self.elem.send_keys("an5t32")
            self.elem.submit()
            if (captcha.is_displayed()):
                self.elem = None
                return True

    def throw_captcha(self):
        self.elem = self.driver.find_element_by_name("Email")
        WebDriverWait(self.driver, 10).until(
            lambda s: self.__infinity_email_loop()
        )


