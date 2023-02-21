from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    for divisor in range(2, num // 2 + 1):
        if num % divisor == 0:
            return False
    return True


def generate_question_n_answer():
    random_num = randint(1, 100)
    correct_answer = 'yes' if is_prime(random_num) else 'no'
    return random_num, correct_answer
