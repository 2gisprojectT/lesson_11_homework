from base_component import BaseComponent

class ElementsForm(BaseComponent):
     selectors = {
         'Name': 'FirstName',
         'LastName': 'LastName',
         'Email': 'GmailAddress',
         'Button': 'submitbutton',
         'errormsg': 'errormsg_0_GmailAddress',
         'passwd': 'Passwd',
         'errormsg_pd': 'errormsg_0_Passwd',
         'captcha': 'recaptcha_challenge_image',
         'check': 'SkipCaptcha'
        }

     def inputN(self, q):
          self.driver.find_element_by_id(self.selectors['Name']).send_keys(q)

     def inputL(self,q):
          self.driver.find_element_by_id(self.selectors['LastName']).send_keys(q)

     def inputEmail(self,q):
          self.driver.find_element_by_id(self.selectors['Email']).send_keys(q)

     def submit_button(self):
          self.driver.find_element_by_id(self.selectors['Button']).submit()

     def inputPD(self,q):
          self.driver.find_element_by_id(self.selectors['passwd']).send_keys(q)

     def get_errorEmail(self):
       return self.driver.find_element_by_id(self.selectors['errormsg']).text

     def get_errorPD(self):
       return self.driver.find_element_by_id(self.selectors['errormsg_pd']).text

     def get_captcha(self):
         return self.driver.find_element_by_id(self.selectors['captcha']).is_displayed

     def check_captcha(self):
         self.driver.find_element_by_id(self.selectors['check']).click()
