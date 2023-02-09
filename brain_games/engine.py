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


def start_game(generator, rules, username):
    for i in range(1, 4):
        question, correct_answer = generator()
        print(rules)
        if not answer_question(question, correct_answer, i, username):
            break
