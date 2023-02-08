from brain_games.cli import welcome_user
from engine import start_game


def is_prime(num):
    for divisor in range(2, num // 2 + 1):
        if num % divisor == 0:
            return 'no'
    return 'yes'


def guess_is_prime(username):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    start_game((1, 100), None, None, is_prime, username)


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    guess_is_prime(username)


if __name__ == '__main__':
    main()
