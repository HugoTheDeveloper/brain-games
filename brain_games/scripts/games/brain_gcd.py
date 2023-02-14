from brain_games.cli import welcome_user
from brain_games.engine import launch_game
from brain_games.scripts import brain_gcd_script


def guess_greater_divisor(username):
    launch_game(brain_gcd_script, username)


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    guess_greater_divisor(username)


if __name__ == '__main__':
    main()
