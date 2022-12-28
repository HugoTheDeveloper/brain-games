#!/usr/bin/env python3
from random import randint
import prompt
from brain_games.cli import welcome_user, name_list


def create_progression():
    first_num = randint(5, 10)
    step = randint(2, 7)
    progression = []
    i1 = 1
    while i1 <= step + 4:
        progression.append(first_num + step * i1)
        i1 += 1
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
    i = 0
    while i < 3:
        first_num = randint(3, 10)
        step = randint(2, 8)
        progression = []
        i1 = 1
        while i1 <= step + 4:
            progression.append(first_num + step * i1)
            i1 += 1
        random_index = randint(1, len(progression) - 2)
        correct_answer = str(progression[random_index])
        progression.pop(random_index)
        progression.insert(random_index, '..')
        answer = prompt.string(f'Question: {transform_lst_to_str(progression)}\nYour answer: ')
        if answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is a wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name_list[0]}!")
            break
        if i == 3:
            print(f'Congratulations, {name_list[0]}!')


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    guess_absent_num()


if __name__ == '__main__':
    main()
