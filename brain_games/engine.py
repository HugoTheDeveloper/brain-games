import prompt


def greet():
    '''
    Greet person, ask his name and return it
    '''

    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    return username


def launch_game(game):
    '''
    Greet user, print rules of the game. Ask questions from the arg, compare
    it and so on for 3 times. If user do mistake, func print correct answer and
    finish. Otherwise, if user will answer correct for 3 times, func congratulate user
    and finish.
    :param game: module, which return question and correct answer
    :return: None
    '''
    username = greet()
    print(game.RULE)
    for i in range(1, 4):
        question, correct_answer = \
            game.generate_question_n_answer()
        answer = prompt.string(f'Question: {question}\nYour answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is a wrong answer ;("
                  f". Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            break
        if i == 3:
            print(f'Congratulations, {username}!')
