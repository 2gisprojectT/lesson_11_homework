from base_component import BaseComponent

class CaptchaForm(BaseComponent):

    selectors = {
        'input_captcha':  "//input[@name='recaptcha_response']",
        'reload_captcha': "//img[contains(@data-reactid,'.0.3.0.0')]",
        'sound_captcha': "//img[contains(@data-reactid,'.0.3.1.0')]",
        'info_captcha': "//img[contains(@data-reactid,'.0.3.3.0')]"
    }

    def info_about_captcha(self):
        self.driver.find_element_by_xpath(self.selectors['info_captcha']).click()