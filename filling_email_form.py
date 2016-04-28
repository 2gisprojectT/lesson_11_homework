from selenium.webdriver.support.ui import WebDriverWait

from base_component import Base_Component


class FillingEmailForm(Base_Component):
    def enter_email(self, email_input):
        self.elem = self.driver.find_element_by_name("Email")
        self.elem.send_keys(email_input)
        self.elem.submit()

    def get_error(self):
        return self.driver.find_element_by_css_selector(".has-error .error-msg").text

    def __enter_email_loop(self):
        while (True):
            self.elem.send_keys("an5t32")
            self.elem.submit()
            if (self.captcha.is_displayed()):
                self.elem = None
                return True

    def send_email_some_seconds(self, time):
        self.elem = self.driver.find_element_by_name("Email")
        self.captcha = self.driver.find_element_by_id("captcha-img")
        try:
            WebDriverWait(self.driver, time).until(
                lambda ec: self.__enter_email_loop()
            )
        except:
            print("Программа работала слишком долго")
        finally:
            return self.captcha.is_displayed
