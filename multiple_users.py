from models import Session, User
from faker import Faker


def create_fake_users(count=10):
    fake = Faker()
    return [
        User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email()
        )
    for _ in range(count)
    ]



def main():
    session = Session()

    users = create_fake_users()

    session.add_all(users)
    session.commit()

if __name__ == '__main__':
    main()