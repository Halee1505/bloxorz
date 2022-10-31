import sys
import time
from input import get_start_game
from algorithm import dfs
from draw import draw


def print_state(state):
    print("--------------------------")
    print((state.goal.x, state.goal.y))
    print((state.block.node1.x, state.block.node1.y))
    print((state.block.node2.x, state.block.node2.y))


def __main__():
    game = get_start_game()
    game1 = get_start_game()

    step = []

    game = dfs(game)
    getParent = game
    while getParent is not None:
        step.append(getParent)
        getParent = getParent.parent
    step.reverse()
    # for i in step:
    #     print_state(i)
    draw(game1, step)


__main__()
