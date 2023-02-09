from brain_games.cli import welcome_user
from brain_games.engine import start_game, get_random_num


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    for divisor in range(2, num // 2 + 1):
        if num % divisor == 0:
            return 'no'
    return 'yes'


def generate_q_and_a():
    random_num = get_random_num(1, 100)
    correct_answer = is_prime(random_num)
    return random_num, correct_answer


def guess_is_prime(username):
    start_game(generate_q_and_a, RULE, username)


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    guess_is_prime(username)


if __name__ == '__main__':
    main()
