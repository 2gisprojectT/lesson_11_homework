from base_component import BaseComponent
from datetime import datetime


class RequestEditForm(BaseComponent):
    selectors = {
        'self': 'db-modal-box',
        'file_name': 'drops_title',
        'set_folder_button': 'create-edit-form-destination-change',
        'new_folder': ".//span[@data-reactid='.3.1.0.0.2.0.1.0.0.0.0.1.$/",
        'set_folder': 'create-edit-form-destination-change',
        'deadlines_checkbox': 'enable-deadlines-checkbox',
        'calendar': 'c-input',
        'calendar_right': 'c-arrow--right',
        'time_selector': 'c-time-selector',
        "deadline_overdue": ".//a[@data-reactid='.3.1.0.0.2.0.2.$deadline-description.0.1']",
        "deadline_overdue_selector": 'c-deadlines__grace-period-selector',
        'save': 'button-primary',
        'notify': 'notify-msg',
    }

    def set_file_name(self, value):
        self.driver.find_element_by_name(self.selectors['file_name']).send_keys(value)

    def set_folder(self, value):
        self.driver.find_element_by_class_name(self.selectors['set_folder_button']).click()
        self.driver.find_element_by_xpath(self.selectors['new_folder']+value+".0']").click()
        self.driver.find_element_by_class_name(self.selectors['set_folder']).click()

    def get_file_name(self):
        return self.driver.find_element_by_name(self.selectors['file_name']).get_attribute("value")

    def set_deadline(self, date, time):
        checkbox = self.driver.find_element_by_id(self.selectors['deadlines_checkbox'])
        if not checkbox.is_selected():
            checkbox.click()
        self.driver.find_element_by_class_name(self.selectors['calendar']).click()
        for i in range(datetime.today().year * 12 + datetime.today().month, date.year * 12 + date.month):
            self.driver.find_element_by_class_name(self.selectors['calendar_right']).click()
        self.driver.find_element_by_id("day" + str(date.day) + "-" + str(date.month - 1)).click()
        self.driver.find_element_by_class_name(self.selectors['time_selector']).click()
        self.driver.find_element_by_xpath(".//div[@title='" + time + " ']").click()

    def set_deadline_overdue(self, value):
        deadline_overdue = self.driver.find_element_by_xpath(self.selectors["deadline_overdue"])
        if deadline_overdue.is_displayed():
            deadline_overdue.click()
        self.driver.find_element_by_class_name(self.selectors["deadline_overdue_selector"]).click()
        self.driver.find_element_by_xpath(".//div[@title='"+value+"']").click()

    def get_notify(self):
        return self.driver.find_element_by_id(self.selectors["notify"]).text

    def save(self):
        self.driver.find_element_by_class_name(self.selectors['save']).click()



