from brain_games.cli import welcome_user
from brain_games.engine import start_game, get_random_num


RULE = 'Find the greatest common divisor of given numbers.'


def find_great_divisor(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def generate_q_and_a():
    random_num = get_random_num(1, 100)
    random_num2 = get_random_num(1, 50)
    question = f'{random_num} {random_num2}'
    correct_answer = find_great_divisor(random_num, random_num2)
    return question, correct_answer


def guess_greater_divisor(username):
    start_game(generate_q_and_a, RULE, username)


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    guess_greater_divisor(username)


if __name__ == '__main__':
    main()
