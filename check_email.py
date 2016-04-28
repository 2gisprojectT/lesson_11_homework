from base_component import BaseComponent

class CheckEmail(BaseComponent):
     selectors = {
         'Email': 'GmailAddress',
         'errormsg': 'errormsg_0_GmailAddress',
     }

     def get_email(self,text):
          self.driver.find_element_by_id(self.selectors['Email']).send_keys(text)

     def get_error_email(self):
       return self.driver.find_element_by_id(self.selectors['errormsg']).text