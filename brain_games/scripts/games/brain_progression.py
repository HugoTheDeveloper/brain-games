from random import randint
from brain_games.cli import welcome_user
from brain_games.engine import start_game, get_random_num


RULE = 'What number is missing in the progression?'


def create_progression(first_num, step):
    progression = []
    i = 1
    while i <= step + 4:
        progression.append(str(first_num + step * i))
        i += 1
    return progression


def generate_q_and_a():
    random_num = get_random_num(3, 10)
    step = get_random_num(2, 8)
    progression = create_progression(random_num, step)
    random_index = randint(1, len(progression) - 2)
    correct_answer = str(progression[random_index])
    progression.pop(random_index)
    progression.insert(random_index, '..')
    question = " ".join(progression)
    return question, correct_answer


def guess_absent_num(username):
    start_game(generate_q_and_a, RULE, username)


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    guess_absent_num(username)


if __name__ == '__main__':
    main()
