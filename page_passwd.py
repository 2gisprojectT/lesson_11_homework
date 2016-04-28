class PagePasswd:
   def __init__(self, driver):
        self.driver = driver
        self._input_passwd=None

   @property
   def input_passwd(self):
       from check_passwd import CheckPasswd

       if self._input_passwd is None:
         self._input_passwd = CheckPasswd(self.driver)
       return self._input_passwd
