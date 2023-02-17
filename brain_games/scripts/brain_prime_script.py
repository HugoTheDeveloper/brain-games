from brain_games.engine import launch_game
from brain_games.games import brain_prime


def guess_is_prime():
    launch_game(brain_prime)


def main():
    guess_is_prime()


if __name__ == '__main__':
    main()
