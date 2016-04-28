from base_component import BaseComponent

class SentRequest(BaseComponent):
     selectors = {
       'Button': 'submitbutton',
     }

     def submit_button(self):
          self.driver.find_element_by_id(self.selectors['Button']).submit()