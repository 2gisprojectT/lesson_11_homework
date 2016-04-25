from selenium.common.exceptions import NoSuchElementException

from BaseComponent import BaseComponent


class CreateEditForm(BaseComponent):
    selectors = {
        "name": "drops_title",
        "errorWrapper": "text-input-error-wrapper",
        "deadlineCheckbox": "enable-deadlines-checkbox",
        "afterDeadlineUploadLink": ".//a[@data-reactid='.3.1.0.0.2.0.2.$deadline-description.0.1']",
        "periodSelector": ".//div[@data-reactid='.3.1.0.0.2.0.2.$deadline-description2.1.2.0']",
        "nextBtn": "button-primary",
        "closeBtn": ".//button[@data-reactid='.3.1.0.0.0']"
    }

    def fill_form(self, name, period=None):
        self.set_name(name)
        if period is not None:
            self.set_deadline_flag(True)
            self.set_after_deadline_download_period(period)
        self.next_step()

    def set_name(self, name):
        self.driver.find_element_by_name(self.selectors["name"]).send_keys(name)

    def get_name(self):
        return self.driver.find_element_by_name(self.selectors["name"]).get_attribute("value")

    def get_error(self):
        return self.driver.find_element_by_class_name(self.selectors["errorWrapper"]).text

    def set_deadline_flag(self, flag):
        checkbox = self.driver.find_element_by_id(self.selectors["deadlineCheckbox"])
        if checkbox.is_selected() ^ flag:
            checkbox.click()

    def get_deadline_flag(self):
        return self.driver.find_element_by_id(self.selectors["deadlineCheckbox"]).is_selected()

    def set_after_deadline_download_period(self, period):
        link = self.driver.find_element_by_xpath(self.selectors["afterDeadlineUploadLink"])
        if link.is_displayed():
            link.click()
        self.driver.find_element_by_xpath(self.selectors["periodSelector"]).click()
        period_selector = ".//div[@title='" + period + "']"
        self.driver.find_element_by_xpath(period_selector).click()

    def get_after_deadline_download_period(self):
        if self.is_exist_after_deadline_upload_period():
            return self.driver.find_element_by_xpath(self.selectors["periodSelector"]).get_attribute("title")
        return None

    def is_exist_after_deadline_upload_period(self):
        try:
            self.driver.find_element_by_xpath(self.selectors["afterDeadlineUploadLink"])
        except NoSuchElementException:
            return self.get_deadline_flag()
        return False

    def next_step(self):
        self.driver.find_element_by_class_name(self.selectors["nextBtn"]).click()

    def close(self):
        self.driver.find_element_by_xpath(self.selectors["closeBtn"]).click()
