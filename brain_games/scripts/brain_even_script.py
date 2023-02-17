from brain_games.engine import launch_game
from brain_games.games import brain_even


def guess_is_even_num():
    launch_game(brain_even)


def main():
    guess_is_even_num()


if __name__ == '__main__':
    main()
