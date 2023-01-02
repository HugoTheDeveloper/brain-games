from random import randint
import prompt
from brain_games.cli import welcome_user
from engine import \
    congratulate_user, is_answer_correct


def find_great_divisor(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def guess_greater_divisor():
    print('Find the greatest common divisor of given numbers.')
    for i in range(1, 4):
        num1 = randint(1, 100)
        num2 = randint(1, 50)
        answer = prompt.string(f'Question: {num1} {num2}\nYour answer: ')
        correct_answer = str(find_great_divisor(num1, num2))
        if not(is_answer_correct(answer, correct_answer)):
            break
        congratulate_user(i)


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    guess_greater_divisor()


if __name__ == '__main__':
    main()
