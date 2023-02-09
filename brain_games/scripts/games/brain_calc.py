from brain_games.cli import welcome_user
from brain_games.engine import start_game, get_random_num, get_random_operator
from operator import mul, sub, add


RULE = 'What is the result of the expression?'


def operate_nums(num1, num2, operator):
    operators_dic = {'+': add, '-': sub, '*': mul}
    correct_answer = operators_dic[operator](num1, num2)
    return correct_answer


def generate_q_and_a():
    random_num = get_random_num(1, 25)
    random_num2 = get_random_num(1, 25)
    random_operator = get_random_operator()
    question = f'{random_num} {random_operator} {random_num2}'
    correct_answer = operate_nums(random_num, random_num2, random_operator)
    return question, correct_answer


def calculate(username):
    start_game(generate_q_and_a, RULE, username)


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    calculate(username)


if __name__ == '__main__':
    main()
