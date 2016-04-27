class PageAuth:
   def __init__(self, driver):
        self.driver = driver
        self._input_form=None

   @property
   def input_form(self):
       from elements_form import ElementsForm

       if self._input_form is None:
         self._input_form = ElementsForm(self.driver)
       return self._input_form


   def open(self, url):
       self.driver.get(url)