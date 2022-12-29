#!/usr/bin/env python3
from random import randint
import prompt
from brain_games.cli import welcome_user
from brain_games.scripts.standard_answers import congratulate_user, is_answer_correct


def is_even_num(num):
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def guess_is_even_num():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(1, 4):
        random_number = randint(1, 100)
        correct_answer = is_even_num(random_number)
        answer = prompt.string(f'Question: {random_number}\nYour answer: ')
        if is_answer_correct(answer, correct_answer):
            break
        congratulate_user(i)


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    guess_is_even_num()


if __name__ == '__main__':
    main()
