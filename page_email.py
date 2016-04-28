class PageEmail:
   def __init__(self, driver):
        self.driver = driver
        self._input_email=None

   @property
   def input_email(self):
       from check_email import CheckEmail

       if self._input_email is None:
         self._input_email = CheckEmail(self.driver)
       return self._input_email
