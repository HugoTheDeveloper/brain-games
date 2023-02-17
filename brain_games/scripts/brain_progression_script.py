from brain_games.engine import launch_game
from brain_games.games import brain_progression


def guess_absent_num():
    launch_game(brain_progression)


def main():
    guess_absent_num()


if __name__ == '__main__':
    main()
