import time


def print_state(state):
    print("--------------------------")
    print(((state.block.node1.x, state.block.node1.y),
          (state.block.node2.x, state.block.node2.y)))
    print("--------------------------")


def dfs(init_state):
    stack = []
    stack.append(init_state)
    visited = set()
    ind = 0

    print("start a new state")
    while stack:
        curr_state = stack.pop()
        if curr_state.finish() is True:
            return curr_state
        if curr_state.block.string_block() not in visited:
            visited.add(curr_state.block.string_block())
            for next_state in curr_state.move():
                stack.append(next_state)
        #     print(len(curr_state.move()))
        # ind += 1
        # if ind == 1:
        #     return curr_state
        # time.sleep(1)
