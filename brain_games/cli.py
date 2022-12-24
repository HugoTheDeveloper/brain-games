import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


if __name__ == '__main__':
    welcome_user()
