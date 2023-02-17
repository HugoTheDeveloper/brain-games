from brain_games.engine import launch_game
from brain_games.games import brain_gcd


def guess_greater_divisor():
    launch_game(brain_gcd)


def main():
    guess_greater_divisor()


if __name__ == '__main__':
    main()
