from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_num(num):
    '''
    Check is even num or not
    :param num: int
    :return: bool
    '''
    if num % 2 == 0:
        return True
    else:
        return False


def generate_question_n_answer():
    '''
    Make random num, check is it even
    :return: question(int), correct answer(str)
    '''
    random_num = randint(1, 100)
    correct_answer = 'yes' if is_even_num(random_num) else 'no'
    return random_num, correct_answer
