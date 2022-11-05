import sys
import time
from input import get_start_game
from algorithm import genetic_algorithm


def run_game(level):
    game = get_start_game(level)
    genetic_algorithm(game, 10)


def main(type='one'):
    level = 2
    run_game(level)


if __name__ == "__main__":
    main()
