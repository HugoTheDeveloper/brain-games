from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_num(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generate_question_n_answer():
    random_num = randint(1, 100)
    correct_answer = is_even_num(random_num)
    return random_num, correct_answer
