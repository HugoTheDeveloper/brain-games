from random import randint
import prompt
from brain_games.cli import welcome_user
from engine import \
    is_answer_correct, congratulate_user


def create_progression(first_num, step):
    progression = []
    i = 1
    while i <= step + 4:
        progression.append(str(first_num + step * i))
        i += 1
    return progression


def transform_lst_to_str(progression):
    progression_str = ''
    i = 0
    while len(progression) > i:
        progression_str += ' ' + str(progression[i])
        i += 1
    return progression_str.strip()


def guess_absent_num():
    print('What number is missing in the progression?')
    for i in range(1, 4):
        first_num = randint(3, 10)
        step = randint(2, 8)
        progression = create_progression(first_num, step)
        random_index = randint(1, len(progression) - 2)
        correct_answer = str(progression[random_index])
        progression.pop(random_index)
        progression.insert(random_index, '..')
        answer = prompt.string(f'Question: \
{transform_lst_to_str(progression)}\nYour answer: ')
        if not(is_answer_correct(answer, correct_answer)):
            break
        congratulate_user(i)


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    guess_absent_num()


if __name__ == '__main__':
    main()
