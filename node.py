# bloxorz game


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Block:
    def __init__(self, node1, node2):
        self.node1 = Node(node1.x, node1.y)
        self.node2 = Node(node2.x, node2.y)

    def string_block(self):
        return str(self.node1.x) + str(self.node1.y) + str(self.node2.x) + str(self.node2.y)

    def finish(self, goal):
        if self.node1.x == self.node2.x and self.node1.y == self.node2.y and self.node1.x == goal.x and self.node1.y == goal.y:
            return True
        else:
            return False
