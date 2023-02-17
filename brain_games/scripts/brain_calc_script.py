from brain_games.engine import launch_game
from brain_games.games import brain_calc


def calculate():
    launch_game(brain_calc)


def main():
    calculate()


if __name__ == '__main__':
    main()
