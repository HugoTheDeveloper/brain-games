from random import randint
import prompt
from brain_games.cli import welcome_user
from engine import \
    congratulate_user, is_answer_correct


def is_prime(num):
    for divisor in range(2, num // 2 + 1):
        if num % divisor == 0:
            return False
    return True


def guess_is_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(1, 4):
        random_num = randint(1, 60)
        if is_prime(random_num):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        answer = prompt.string(f'Question: {random_num}\nYour answer: ')
        if not(is_answer_correct(answer, correct_answer)):
            break
        congratulate_user(i)


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    guess_is_prime()


if __name__ == '__main__':
    main()
