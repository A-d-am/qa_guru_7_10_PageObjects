from selene import browser, have


# noinspection PyMethodMayBeStatic
class LeftPanel:
    def open(self, value):
        browser.all('.menu-list span').element_by(have.exact_text(value)).click()

    def open_simple_registration_form(self):
        self.open('Text Box')
