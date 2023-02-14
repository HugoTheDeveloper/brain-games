from brain_games.cli import welcome_user
from brain_games.engine import launch_game
from brain_games.scripts import brain_calc_script


def calculate(username):
    launch_game(brain_calc_script, username)


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    calculate(username)


if __name__ == '__main__':
    main()
