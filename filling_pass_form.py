from head import Head


class FillingPassForm(Head):
    def enter_passw(self, passw_input):
        passwd = self.driver.find_element_by_name("Passwd")
        passwd.send_keys(passw_input)
        passwd.submit()

    def get_error(self):
        return self.driver.find_element_by_id("errormsg_0_Passwd").text
