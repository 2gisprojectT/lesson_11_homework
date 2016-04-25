from Base_component import BaseComponent
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Flight(BaseComponent):

    selector = {
        'flight': '//*[@id="FirstPrefered"]/div/div/div[3]/button'
    }

    def chosing_flight(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.selector['flight']))).click()