from brain_games.cli import welcome_user
from engine import start_game


def find_great_divisor(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def guess_greater_divisor(username):
    print('Find the greatest common divisor of given numbers.')
    start_game((1, 100), (1, 50), None, find_great_divisor, username)


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    guess_greater_divisor(username)


if __name__ == '__main__':
    main()
