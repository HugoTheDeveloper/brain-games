from brain_games.cli import welcome_user
from engine import start_game


def is_even_num(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def guess_is_even_num(username):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start_game((1, 100), None, None, is_even_num, username)


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    guess_is_even_num(username)


if __name__ == '__main__':
    main()
