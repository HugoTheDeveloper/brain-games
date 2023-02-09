from brain_games.cli import welcome_user
from brain_games.engine import start_game, get_random_num


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_num(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generate_q_and_a():
    random_num = get_random_num(1, 100)
    correct_answer = is_even_num(random_num)
    return random_num, correct_answer


def guess_is_even_num(username):
    start_game(generate_q_and_a, RULE, username)


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    guess_is_even_num(username)


if __name__ == '__main__':
    main()
