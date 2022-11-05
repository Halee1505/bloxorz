import sys
import time
from input import get_start_game
from algorithm import dfs
from draw import draw


def get_step(step):
    move = ""
    print("Total step: ", len(step)-1)
    for i in step:
        move += i.direction + "-> "
    print(move)


def get_step_demo(step):
    print("Total step: ", len(step)-1)
    # for i in step:
    #     print(i.direction)


def run_game(level, mode='auto', draw_mode=0):
    game = get_start_game(level)
    start = game.block.node1
    goal = game.goal
    step = []
    game = dfs(game)
    getParent = game
    while getParent is not None:
        step.append(getParent)
        getParent = getParent.parent
    step.reverse()
    get_step_demo(step)
    if draw_mode == str(1):
        draw(step, start, goal, mode)


def main(type='one', mode='auto', draw_mode=0):
    if type == 'one':
        print("Choose level:")
        level = int(input())
        run_game(level, mode, draw_mode)
    elif type == 'all':
        for level in range(1, 8):
            print("level: ", level)
            run_game(level, mode, draw_mode)
            print("_____________________")


if __name__ == "__main__":
    if len(sys.argv) > 3:
        type = sys.argv[1]
        mode = sys.argv[2]
        draw_mode = sys.argv[3]
        if type == 'one':
            main(type='one', mode=mode, draw_mode=draw_mode)
        elif type == 'all':
            main(type='all', mode=mode, draw_mode=draw_mode)
    else:
        # Edit here
        main(type='all', mode='auto', draw_mode=0)
