from Base_component import BaseComponent
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Flight(BaseComponent):

    selectors = {
        'flight': '//*[@id="FirstPrefered"]/div/div/div[3]/button'
    }

    def select_flight(self):
        self.driver.find_element_by_xpath(self.selectors['flight']).click()