from CreateEditForm import CreateEditForm
from DropsManagementGrid import DropsManagementGrid
from ShareRequestForm import ShareRequestForm


class PageRequests:
    def __init__(self, driver):
        self.driver = driver
        self._drops_management_grid = None
        self._create_edit_form = None
        self._share_request_form = None

    @property
    def drops_management_grid(self):
        if self._drops_management_grid is None:
            self._drops_management_grid = DropsManagementGrid(self.driver)
        return self._drops_management_grid

    @property
    def create_edit_form(self):
        if self._create_edit_form is None:
            self._create_edit_form = CreateEditForm(self.driver)
        return self._create_edit_form

    @property
    def share_request_form(self):
        if self._share_request_form is None:
            self._share_request_form = ShareRequestForm(self.driver)
        return self._share_request_form

    def open(self, url):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()