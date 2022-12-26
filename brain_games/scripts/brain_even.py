#!/usr/bin/env python3
from random import randint
import prompt
from brain_games.cli import welcome_user, name_list


def guess_is_even_num():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = randint(1, 100)
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        answer = prompt.string(f'Question: {random_number}\nYour answer: ')
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
    guess_is_even_num()


if __name__ == '__main__':
    main()
