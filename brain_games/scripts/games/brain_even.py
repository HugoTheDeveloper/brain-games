from brain_games.cli import welcome_user
from brain_games.engine import launch_game
from brain_games.scripts import brain_even_script


def guess_is_even_num(username):
    launch_game(brain_even_script, username)


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    guess_is_even_num(username)


if __name__ == '__main__':
    main()
