from game import Game
from node import Node, Block

data1 = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 1], [4, 2], [4, 3], [
    5, 1], [5, 2], [5, 3], [5, 4], [6, 2], [6, 3], [6, 4], [6, 5], [7, 2], [7, 3], [7, 4], [7, 5], [8, 2], [8, 3], [8, 4], [8, 5], [9, 3], [9, 4]]

data2 = [
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [0, 5],
    [1, 1],
    [1, 2],
    [1, 3],
    [1, 4],
    [1, 5],
    [2, 1],
    [2, 2],
    [2, 3],
    [2, 4],
    [2, 5],
    [3, 1],
    [3, 2],
    [3, 3],
    [3, 4],
    [3, 5],

    [5, 4],
    [4, 4],

    [6, 0],
    [6, 1],
    [6, 2],
    [6, 3],
    [6, 4],
    [6, 5],
    [7, 0],
    [7, 1],
    [7, 2],
    [7, 3],
    [7, 4],
    [7, 5],
    [8, 0],
    [8, 1],
    [8, 2],
    [8, 3],
    [8, 4],
    [8, 5],
    [9, 0],
    [9, 1],
    [9, 2],
    [9, 3],
    [9, 4],
    [9, 5],

    [11, 4],
    [10, 4],

    [12, 0],
    [12, 1],
    [12, 2],
    [12, 3],
    [12, 4],
    [13, 0],
    [13, 1],
    [13, 2],
    [13, 3],
    [13, 4],
    [14, 0],
    [14, 1],
    [14, 2],
    [14, 3],
    [14, 4],

]


def get_start_game():
    map = []
    for i in range(16):
        map.append([" "] * 16)
    for i in data2:
        map[i[0]][i[1]] = "x"
    start = Node(1, 4)
    goal = Node(13, 1)
    game = Game(map, Block(start, start),  goal, None)
    return game


if __name__ == '__main__':
    get_start_game()