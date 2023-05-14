from random import choice

from models import Session, User


def main():
    session = Session()
    users = session.query(User).all()

    lucky_user = choice(users)
    print(f"And the lucky winner is {lucky_user} with id {lucky_user.id}")

    prev_salary = lucky_user.salary
    lucky_user.salary *= 1.15

    print(f'His/Her salary grow from {prev_salary} to {lucky_user.salary}')
    session.add(lucky_user)
    session.commit()

    result = session.query(User).get(lucky_user.id)
    assert result.salary != prev_salary, "Salary was not updated"

if __name__ == '__main__':
    main()
