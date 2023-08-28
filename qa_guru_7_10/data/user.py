from dataclasses import dataclass


@dataclass
class User:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


test_user = User(
    full_name='Ivanov Ivan',
    email='user@asdasd.com',
    current_address='Pushkina street, Moscow',
    permanent_address='Kolotushkina avenue, Moscow'
)
