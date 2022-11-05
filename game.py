from node import Node, Block


def print_state(state):
    print("--------------------------")
    print((state.goal.x, state.goal.y))
    print((state.block.node1.x, state.block.node1.y))
    print((state.block.node2.x, state.block.node2.y))
    print("--------------------------")


class Game:

    MIN_X = 0
    MIN_Y = 0
    MAX_X = 15
    MAX_Y = 15

    def __init__(self, map, block,  goal, parent, direction="Go"):
        self.map = map
        self.goal = goal
        self.block = block
        self.parent = parent
        self.direction = direction

    def can_move(self, x, y):
        if x <= self.MAX_X and x >= self.MIN_X and y <= self.MAX_Y and y >= self.MIN_Y and self.map[x][y] == 'x':
            return True
        else:
            return False

    def move(self):
        next_states = []
        x1 = self.block.node1.x
        y1 = self.block.node1.y
        x2 = self.block.node2.x
        y2 = self.block.node2.y

        if x1 == x2 and y1 == y2:  # block chong nhau
            if self.can_move(x1, y1-1) and self.can_move(x2, y2-2):
                new_block = Block(Node(x2, y2-2), Node(x1, y1-1))
                next_states.append(
                    Game(self.map, new_block, self.goal, self, "Up"))
            if self.can_move(x1, y1+1) and self.can_move(x2, y2+2):
                new_block = Block(Node(x1, y1+1), Node(x2, y2+2))
                next_states.append(
                    Game(self.map, new_block, self.goal, self, "Down"))
            if self.can_move(x1-1, y1) and self.can_move(x2-2, y2):
                new_block = Block(Node(x2-2, y2), Node(x1-1, y1))
                next_states.append(
                    Game(self.map, new_block, self.goal, self, "Left"))
            if self.can_move(x1+1, y1) and self.can_move(x2+2, y2):
                new_block = Block(Node(x1+1, y1), Node(x2+2, y2))
                next_states.append(
                    Game(self.map, new_block, self.goal, self, "Right"))
        elif x1 == x2:  # block nam tren 1 hang
            if self.can_move(x1, y1-1) and self.can_move(x2, y2-2):
                new_block = Block(Node(x2, y2-2), Node(x1, y1-1))
                next_states.append(
                    Game(self.map, new_block, self.goal, self, "Up"))
            if self.can_move(x1, y1+2) and self.can_move(x2, y2+1):
                new_block = Block(Node(x2, y2+1), Node(x1, y1+2))
                next_states.append(
                    Game(self.map, new_block, self.goal, self, "Down"))
            if self.can_move(x1-1, y1) and self.can_move(x2-1, y2):
                new_block = Block(Node(x1-1, y1), Node(x2-1, y2))
                next_states.append(
                    Game(self.map, new_block, self.goal, self, "Left"))
            if self.can_move(x1+1, y1) and self.can_move(x2+1, y2):
                new_block = Block(Node(x1+1, y1), Node(x2+1, y2))
                next_states.append(
                    Game(self.map, new_block, self.goal, self, "Right"))
        elif y1 == y2:  # block nam tren 1 cot
            if self.can_move(x1, y1-1) and self.can_move(x2, y2-1):
                new_block = Block(Node(x1, y1-1), Node(x2, y2-1))
                next_states.append(
                    Game(self.map, new_block, self.goal, self, "Up"))
            if self.can_move(x1, y1+1) and self.can_move(x2, y2+1):
                new_block = Block(Node(x1, y1+1), Node(x2, y2+1))
                next_states.append(
                    Game(self.map, new_block, self.goal, self, "Down"))
            if self.can_move(x1-1, y1) and self.can_move(x2-2, y2):
                new_block = Block(Node(x2-2, y2), Node(x1-1, y1))
                next_states.append(
                    Game(self.map, new_block, self.goal, self, "Left"))
            if self.can_move(x1+2, y1) and self.can_move(x2+1, y2):
                new_block = Block(Node(x2+1, y2), Node(x1+2, y1))
                next_states.append(
                    Game(self.map, new_block, self.goal, self, "Right"))

        return next_states

    def random_move(self):
        next_states = self.move()
        import random
        return_state = random.choice(next_states)
        if(self.parent != None):

            while return_state.block.string_block() == self.parent.block.string_block():
                return_state = random.choice(next_states)

        return return_state

    def finish(self):
        return self.block.finish(self.goal)
