from base_component import Base_Component


class FillingPassForm(Base_Component):
    def enter_passw(self, passw_input):
        self.elem = self.driver.find_element_by_name("Passwd")
        self.elem.send_keys(passw_input)
        self.elem.submit()

    def get_error(self):
        return self.driver.find_element_by_id("errormsg_0_Passwd").text
