from BaseComponent import BaseComponent


class CreateEditForm(BaseComponent):
    selectors = {
        "name": "drops_title",
        "errorWrapper": "text-input-error-wrapper",
        "deadlineCheckbox": "enable-deadlines-checkbox",
        "afterDeadlineUploadLink": ".//a[@data-reactid='.3.1.0.0.2.0.2.$deadline-description.0.1']",
        "periodSelector": ".//div[@data-reactid='.3.1.0.0.2.0.2.$deadline-description2.1.2.0']",
        "nextBtn": "button-primary"
    }

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

    def set_after_deadline_download_period(self, period):
        link = self.driver.find_element_by_xpath(self.selectors["afterDeadlineUploadLink"])
        if link.is_displayed():
            link.click()
        self.driver.find_element_by_xpath(self.selectors["periodSelector"]).click()
        period_selector = ".//div[@title='"+period+"']"
        self.driver.find_element_by_xpath(period_selector).click()

    def get_after_deadline_download_period(self):
        return self.driver.find_element_by_xpath(self.selectors["periodSelector"]).get_attribute("title")

    def is_displayed_after_deadline_upload_link(self):
        return self.driver.find_element_by_xpath(self.selectors["afterDeadlineUploadLink"]).is_displayed()

    def next_step(self):
        self.driver.find_element_by_class_name(self.selectors["nextBtn"]).click()
