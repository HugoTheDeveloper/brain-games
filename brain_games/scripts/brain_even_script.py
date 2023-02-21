#!/usr/bin/env python3
from brain_games.engine import launch_game
from brain_games.games import brain_even


def main():
    launch_game(brain_even)


if __name__ == '__main__':
    main()
