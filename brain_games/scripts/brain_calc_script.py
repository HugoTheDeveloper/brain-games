#!/usr/bin/env python3
from brain_games.engine import launch_game
from brain_games.games import brain_calc


def main():
    launch_game(brain_calc)


if __name__ == '__main__':
    main()
