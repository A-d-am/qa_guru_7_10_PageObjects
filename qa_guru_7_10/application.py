from qa_guru_7_10.model.components.left_panel import LeftPanel
from qa_guru_7_10.model.pages.simple_registration_page import SimpleRegistrationPage
from selene import browser


class Application:

    def __init__(self):
        self.simple_registration = SimpleRegistrationPage()
        self.left_panel = LeftPanel()

    def open(self):
        browser.open('/elements')


app = Application()
