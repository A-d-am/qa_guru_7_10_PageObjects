from selene import browser, have, be,command
from qa_guru_7_10.models.users import User
from conftest import RESOURCES_DIR
import os


# noinspection PyMethodMayBeStatic
class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def type_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def type_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def type_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def set_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def type_mobile(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def type_subjects(self, values):
        for subject in values:
            browser.element('#subjectsInput').should(be.blank).type(subject).press_enter()

    def set_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element(f".react-datepicker__month-select > option[value='{month - 1}']").click()
        browser.element(f".react-datepicker__year-select > option[value='{year}']").click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def set_hobbies(self, values):
        for hobby in values:
            browser.all('.custom-checkbox').element_by(have.exact_text(hobby)).click()

    def upload_picture(self, file_name):
        file_path = os.path.join(RESOURCES_DIR, file_name)
        browser.element('#uploadPicture').send_keys(file_path)

    def type_current_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)

    def set_state_and_city(self, state, city):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(state)).click()

        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(city)).click()

    def submit(self):
        browser.element('#submit').click()

    def should_have_registered(self, user: User):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.mobile,
                user.get_full_birth_date(),
                ', '.join(user.subjects),
                ', '.join(user.hobbies),
                user.picture,
                user.current_address,
                f'{user.state} {user.city}'
            )
        )
