#!/usr/bin/env python3
from random import randint
import prompt
from brain_games.cli import welcome_user, name_list


def is_prime(num):
    for divisor in range(2, num // 2 + 1):
        if num % divisor == 0:
            return False
    return True


def guess_is_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        random_num = randint(1, 60)
        if is_prime(random_num):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        answer = prompt.string(f'Question: {random_num}\nYour answer: ')
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
    guess_is_prime()


if __name__ == '__main__':
    main()
