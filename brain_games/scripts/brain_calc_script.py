from random import randint, choice
from operator import mul, sub, add


RULE = 'What is the result of the expression?'


def operate_nums(num1, num2, operator):
    operators_dic = {'+': add, '-': sub, '*': mul}
    correct_answer = operators_dic[operator](num1, num2)
    return correct_answer


def generate_question_n_answer():
    random_num = randint(1, 25)
    random_num2 = randint(1, 25)
    random_operator = choice(['+', '-', '*'])
    question = f'{random_num} {random_operator} {random_num2}'
    correct_answer = operate_nums(random_num, random_num2, random_operator)
    return question, correct_answer
