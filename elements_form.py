from base_component import BaseComponent

class ElementsForm(BaseComponent):
     selectors = {
         'Name': 'FirstName',
         'LastName': 'LastName',
         'captcha': 'recaptcha_challenge_image',
         'check': 'SkipCaptcha'
        }

     def input_name(self, text):
          self.driver.find_element_by_id(self.selectors['Name']).send_keys(text)

     def input_lastname(self,text):
          self.driver.find_element_by_id(self.selectors['LastName']).send_keys(text)

     def get_captcha(self):
         return self.driver.find_element_by_id(self.selectors['captcha']).is_displayed

     def check_captcha(self):
         self.driver.find_element_by_id(self.selectors['check']).click()
