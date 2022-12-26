#!/usr/bin/env python3
from random import randint, choice
import prompt
from brain_games.cli import welcome_user, name_list


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def guess_greater_divisor():
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        random_num1 = randint(1, 100)
        random_num2 = randint(1, 50)
        answer = prompt.string(f'Question: {random_num1} {random_num2}\nYour answer: ')
        correct_answer = str(gcd(random_num1, random_num2))
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
    guess_greater_divisor()


if __name__ == '__main__':
    main()
