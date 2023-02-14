from random import randint


RULE = 'What number is missing in the progression?'


def create_progression(first_num, step):
    progression = []
    i = 1
    while i <= step + 4:
        progression.append(str(first_num + step * i))
        i += 1
    return progression


def generate_question_n_answer():
    random_num = randint(3, 10)
    step = randint(2, 8)
    progression = create_progression(random_num, step)
    random_index = randint(1, len(progression) - 2)
    correct_answer = str(progression[random_index])
    progression.pop(random_index)
    progression.insert(random_index, '..')
    question = " ".join(progression)
    return question, correct_answer
