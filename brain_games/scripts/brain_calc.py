#!/usr/bin/env python3
from random import randint, choice
import prompt
from brain_games.cli import welcome_user, name_list


def calculate():
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        random_num1 = randint(1, 25)
        random_num2 = randint(1, 25)
        operators_list = ['+', '-', '*']
        random_operator = choice(operators_list)
        answer = prompt.string(f'Question: {random_num1} {random_operator} {random_num2}\nYour answer: ')
        if random_operator == '+':
            correct_answer = str(random_num1 + random_num2)
        elif random_operator == '-':
            correct_answer = str(random_num1 - random_num2)
        else:
            correct_answer = str(random_num1 * random_num2)
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
    calculate()


if __name__ == '__main__':
    main()
