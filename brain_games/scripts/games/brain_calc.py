from brain_games.cli import welcome_user
from engine import start_game
from operator import mul, sub, add


def operate_nums(num1, num2, operator):
    operators_dic = {'+': add, '-': sub, '*': mul}
    correct_answer = operators_dic[operator](num1, num2)
    return correct_answer


def calculate(user_name):
    print('What is the result of the expression?')
    start_game((1, 25), (1, 25), True, operate_nums, user_name)


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    calculate(username)


if __name__ == '__main__':
    main()
