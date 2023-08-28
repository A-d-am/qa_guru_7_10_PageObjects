from selene import browser, have


class LeftPanel:
    def open(self, value):
        browser.all('.menu-list').element_by(have.exact_text(value)).click()
