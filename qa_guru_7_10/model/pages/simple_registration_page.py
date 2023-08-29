from qa_guru_7_10.data.user import User
from selene import browser, have, be


# noinspection PyMethodMayBeStatic
class SimpleRegistrationPage:

    def type_full_name(self, user: User):
        browser.element('#userName').should(be.blank).type(user.full_name)

    def type_email(self, user: User):
        browser.element('#userEmail').should(be.blank).type(user.email)

    def type_current_address(self, user: User):
        browser.element('#currentAddress').should(be.blank).type(user.current_address)

    def type_permanent_address(self, user: User):
        browser.element('#permanentAddress').should(be.blank).type(user.permanent_address)

    def submit(self):
        browser.element('#submit').click()

    def should_have_registered(self, user: User):
        browser.element('#output').should(have.exact_text(
            f'Name:{user.full_name}\n' 
            f'Email:{user.email}\n'
            f'Current Address :{user.current_address}\n'
            f'Permananet Address :{user.permanent_address}'
        ))
        # browser.element('#name').should(have.exact_text(f'Name:{user.full_name}'))
        # browser.element('#email').should(have.exact_text(f'Email:{user.email}'))
        # # browser.element('#currentAddress').should(have.exact_text(f'Current Address :{user.current_address}'))
        # browser.element('#permanentAddress').should(have.exact_text(f'Permananet Address :{user.permanent_address}'))
