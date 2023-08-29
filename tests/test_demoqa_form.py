import os

from qa_guru_7_10.application import app
from qa_guru_7_10.data.user import test_user


def test_simple_registration_page():
    app.open()

    app.open_category('Elements')
    app.left_panel.open_simple_registration_form()

    app.simple_registration.type_full_name(test_user)
    app.simple_registration.type_email(test_user)
    app.simple_registration.type_current_address(test_user)
    app.simple_registration.type_permanent_address(test_user)

    app.simple_registration.submit()

    app.simple_registration.should_have_registered(test_user)
