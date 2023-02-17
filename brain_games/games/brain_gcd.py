from random import randint


RULE = 'Find the greatest common divisor of given numbers.'


def find_great_divisor(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def generate_question_n_answer():
    random_num = randint(1, 100)
    random_num2 = randint(1, 50)
    question = f'{random_num} {random_num2}'
    correct_answer = find_great_divisor(random_num, random_num2)
    return question, correct_answer
