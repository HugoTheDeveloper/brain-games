from random import randint
from brain_games.cli import welcome_user
from engine import answer_question


def create_progression(first_num, step):
    progression = []
    i = 1
    while i <= step + 4:
        progression.append(str(first_num + step * i))
        i += 1
    return progression


def guess_absent_num(username):
    print('What number is missing in the progression?')
    for i in range(1, 4):
        first_num = randint(3, 10)
        step = randint(2, 8)
        progression = create_progression(first_num, step)
        random_index = randint(1, len(progression) - 2)
        correct_answer = str(progression[random_index])
        progression.pop(random_index)
        progression.insert(random_index, '..')
        question = " ".join(progression)
        if answer_question(question, correct_answer, i, username):
            continue
        else:
            break


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    guess_absent_num(username)


if __name__ == '__main__':
    main()
