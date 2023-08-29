from qa_guru_7_10.pages.registration_page import RegistrationPage
import pytest
from qa_guru_7_10.models.users import User


@pytest.fixture()
def user_to_test():
    user_to_test = User(
        first_name='FirstName',
        last_name='LastName',
        email='username@domain.com',
        gender='Male',
        mobile='1234567890',
        date_of_birth_day=17,
        date_of_birth_month=4,
        date_of_birth_year=2000,
        subjects=['Maths', 'Hindi'],
        hobbies=['Sports'],
        picture='test_pict.png',
        current_address='Current address',
        state='NCR',
        city='Delhi'
    )
    return user_to_test


def test_fill_and_send_form(user_to_test):
    registration_page = RegistrationPage()
    registration_page.open()
    # register user
    registration_page.register(user_to_test)
    # Check registered user info
    registration_page.should_have_registered(user_to_test)
