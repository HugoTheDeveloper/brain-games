#!/usr/bin/env python3
from random import randint, choice
import prompt
from brain_games.cli import welcome_user
from brain_games.scripts.standard_answers import congratulate_user, is_answer_correct


def operate_nums(num1, num2, operator):
    if operator == '+':
        correct_answer = str(num1 + num2)
    elif operator == '-':
        correct_answer = str(num1 - num2)
    else:
        correct_answer = str(num1 * num2)
    return correct_answer


def calculate():
    print('What is the result of the expression?')
    for i in range(1, 4):
        random_num1 = randint(1, 25)
        random_num2 = randint(1, 25)
        operators_list = ['+', '-', '*']
        random_operator = choice(operators_list)
        answer = prompt.string(f'Question: {random_num1} {random_operator} {random_num2}\nYour answer: ')
        if is_answer_correct(answer, operate_nums(random_num1, random_num2, random_operator)):
            break
        congratulate_user(i)


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    calculate()


if __name__ == '__main__':
    main()
