class PageRequest:
   def __init__(self, driver):
        self.driver = driver
        self._input_request=None

   @property
   def input_request(self):
       from sent_request import SentRequest

       if self._input_request is None:
         self._input_request = SentRequest(self.driver)
       return self._input_request
