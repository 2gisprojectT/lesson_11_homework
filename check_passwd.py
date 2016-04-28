from base_component import BaseComponent

class CheckPasswd(BaseComponent):
     selectors = {
         'passwd': 'Passwd',
         'errormsg_pd': 'errormsg_0_Passwd'
     }

     def get_passwd(self,text):
        self.driver.find_element_by_id(self.selectors['passwd']).send_keys(text)

     def get_error_passwd(self):
       return self.driver.find_element_by_id(self.selectors['errormsg_pd']).text
