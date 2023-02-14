from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    for divisor in range(2, num // 2 + 1):
        if num % divisor == 0:
            return 'no'
    return 'yes'


def generate_question_n_answer():
    random_num = randint(1, 100)
    correct_answer = is_prime(random_num)
    return random_num, correct_answer
