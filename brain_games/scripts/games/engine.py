import prompt
from random import randint, choice


def get_random_operator():
    operators_list = ['+', '-', '*']
    return choice(operators_list)


def get_random_num(least_limit=1, max_limit=25):
    return randint(least_limit, max_limit)


def is_answer_correct(answer, correct_answer, user_name):
    if answer == str(correct_answer):
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is a wrong answer ;(.\
 Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {user_name}!")
        return False


def congratulate_user(i, user_name):
    if i == 3:
        print(f'Congratulations, {user_name}!')


def answer_question(question, correct_answer, i, user_name):
    answer = prompt.string(f'Question: {question}\nYour answer: ')
    if not (is_answer_correct(answer, correct_answer, user_name)):
        return False
    else:
        congratulate_user(i, user_name)
        return True


def start_game(num1_limit=tuple, num2_limit=None, operator=None,
               checking_func=None, user_name=None):
    for i in range(1, 4):
        min1, max1 = num1_limit
        num1 = get_random_num(min1, max1)
        if operator and num2_limit:
            min2, max2 = num2_limit
            num2 = get_random_num(min2, max2)
            operator = get_random_operator()
            question = f'{num1} {operator} {num2}'
            if answer_question(question, checking_func(num1, num2, operator),
                               i, user_name):
                continue
            else:
                break
        if operator is None and num2_limit:
            min2, max2 = num2_limit
            num2 = get_random_num(min2, max2)
            question = f'{num1} {num2}'
            if answer_question(question, checking_func(num1, num2),
                               i, user_name):
                continue
            else:
                break
        else:
            question = f'{num1}'
            if answer_question(question, checking_func(num1), i, user_name):
                continue
            else:
                break
